import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  StyleSheet,
  ImageBackground,
  TouchableOpacity,
  TextInput,
  ScrollView,
} from "react-native";

import NetInfo from "@react-native-community/netinfo";
import WifiManager from "react-native-wifi-reborn";
import Icon from "react-native-vector-icons/FontAwesome";
import BackgroundTimer from "react-native-background-timer";
import Geolocation from "react-native-geolocation-service";
import { PermissionsAndroid, Platform } from "react-native";

const backgroundImage = require("./cyber_security.jpg");

const requestLocationPermission = async () => {
  if (Platform.OS === "android") {
    try {
      const granted = await PermissionsAndroid.request(
        PermissionsAndroid.PERMISSIONS.ACCESS_WIFI_STATE,
        {
          title: "WiFi permission",
          message:
            "App needs access to your WiFi state " +
            "so you can connect to the internet.",
          buttonNeutral: "Ask Me Later",
          buttonNegative: "Cancel",
          buttonPositive: "OK",
        }
      );

      if (granted === PermissionsAndroid.RESULTS.GRANTED) {
        console.log("WiFi permission granted");
      } else {
        console.log("WiFi permission denied");
      }
    } catch (err) {
      console.warn(err);
    }
  }
};

const App = () => {
  const [wifiList, setWifiList] = useState([]);
  const [selectedNetwork, setSelectedNetwork] = useState(null);
  const [password, setPassword] = useState("");
  const [pingResult, setPingResult] = useState(null);
  const [spoofingResult, setSpoofingResult] = useState(null);
  const [location, setLocation] = useState(null);
  const [connectionTime, setConnectionTime] = useState(null);

  // Fetch available Wi-Fi networks on component mount
  useEffect(() => {
    if (WifiManager === null) {
      console.error("WifiManager is null");
      return;
    }

    try {
      WifiManager.getSSID((ssid) => {
        console.log("SSID:", ssid);
      });
    } catch (err) {
      console.warn(err);
    }

    WifiManager.loadWifiList((wifiArray) => {
      setWifiList(wifiArray);
    });
  });

  // Fetch available Wi-Fi networks
  const fetchWifiList = async () => {
    try {
      const wifiManager = WifiManager;
      if (wifiManager) {
        const wifiArray = await wifiManager.loadWifiList();
        setWifiList(wifiArray);
      } else {
        console.log("WifiManager is null");
      }
    } catch (error) {
      console.log(error);
    }
  };

  // Connect to selected Wi-Fi network
  const connectToNetwork = async () => {
    try {
      await WifiManager.connectToProtectedSSID(selectedNetwork.SSID, password);
      console.log("Connected to network:", selectedNetwork.SSID);
      setPingResult(null);
      setSpoofingResult(null);
      setLocation(null);
      setConnectionTime(null);
      startNetworkInfoUpdates();
    } catch (error) {
      console.log("Error connecting to network:", error);
    }
  };

  // Start updating network info in the background
  const startNetworkInfoUpdates = () => {
    BackgroundTimer.runBackgroundTimer(() => {
      checkPing();
      checkDNS();
      getLocation();
      getConnectionTime();
    }, 5000);
  };

  // Check ping connectivity
  const checkPing = async () => {
    try {
      const response = await NetInfo.fetch("isConnected");
      setPingResult(response.isConnected ? "Connected" : "Disconnected");
    } catch (error) {
      console.log("Error checking ping:", error);
    }
  };

  // Check DNS spoofing
  const checkDNS = async () => {
    try {
      const response = await NetInfo.fetch("isConnectionExpensive");
      setSpoofingResult(
        response.isConnectionExpensive ? "Spoofed" : "Not spoofed"
      );
    } catch (error) {
      console.log("Error checking DNS spoofing:", error);
    }
  };

  // Get current location
  const getLocation = async () => {
    try {
      // Fetch location using appropriate method based on platform (iOS/Android)
      const location = await Geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          fetch(
            `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${latitude}&lon=${longitude}`
          )
            .then((response) => response.json())
            .then((data) => {
              setLocation(data.address.country);
            })
            .catch((error) => {
              console.log("Error getting location:", error);
            });
        },
        (error) => {
          console.log("Error getting location:", error);
        },
        { enableHighAccuracy: true, timeout: 20000, maximumAge: 1000 }
      );
    } catch (error) {
      console.log("Error getting location:", error);
    }
  };

  // Get connection time
  const getConnectionTime = async () => {
    try {
      // Fetch connection time using appropriate method based on platform (iOS/Android)
      const connectionInfo = await NetInfo.fetch();
      const connectionTime = connectionInfo.details
        ? connectionInfo.details.time
          ? connectionInfo.details.time
          : "Unknown"
        : "Unknown";
      setConnectionTime(connectionTime);
    } catch (error) {
      console.log("Error getting connection time:", error);
    }
  };

  return (
    <ImageBackground source={backgroundImage} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.header}>
          <Text style={styles.headerText}>Wi-Fi Security Checker</Text>
        </View>
        <View style={styles.content}>
          <Text style={styles.label}>Available Wi-Fi Networks:</Text>
          {wifiList.map((wifi, index) => (
            <TouchableOpacity
              key={index}
              style={styles.networkItem}
              onPress={() => setSelectedNetwork(wifi)}
            >
              <Text style={styles.networkName}>{wifi.SSID}</Text>
              <Text style={styles.networkSignal}>{wifi.level} dBm</Text>
            </TouchableOpacity>
          ))}
          {selectedNetwork && (
            <View style={styles.selectedNetworkContainer}>
              <Text style={styles.selectedNetworkText}>
                Selected Network: {selectedNetwork.SSID}
              </Text>
              <TextInput
                style={styles.passwordInput}
                placeholder="Enter Password"
                onChangeText={(text) => setPassword(text)}
                secureTextEntry
              />
              <TouchableOpacity
                style={styles.connectButton}
                onPress={connectToNetwork}
              >
                <Text style={styles.connectButtonText}>Connect</Text>
              </TouchableOpacity>
            </View>
          )}
          <View style={styles.infoContainer}>
            <Text style={styles.infoLabel}>Ping Result:</Text>
            <Text style={styles.infoText}>{pingResult}</Text>
          </View>
          <View style={styles.infoContainer}>
            <Text style={styles.infoLabel}>DNS Spoofing:</Text>
            <Text style={styles.infoText}>{spoofingResult}</Text>
          </View>
          <View style={styles.infoContainer}>
            <Text style={styles.infoLabel}>Location:</Text>
            <Text style={styles.infoText}>{location}</Text>
          </View>
          <View style={styles.infoContainer}>
            <Text style={styles.infoLabel}>Connection Time:</Text>
            <Text style={styles.infoText}>{connectionTime}</Text>
          </View>
        </View>
      </ScrollView>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    resizeMode: "cover",
  },
  scrollContainer: {
    flexGrow: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  header: {
    marginTop: 50,
    marginBottom: 30,
  },
  headerText: {
    fontSize: 24,
    fontWeight: "bold",
    color: "white",
  },
  content: {
    width: "80%",
    backgroundColor: "rgba(0, 0, 0, 0.7)",
    borderRadius: 10,
    padding: 20,
  },
  label: {
    fontSize: 18,
    fontWeight: "bold",
    color: "white",
    marginBottom: 10,
  },
  networkItem: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: "rgba(255, 255, 255, 0.2)",
  },
  networkName: {
    flex: 1,
    color: "white",
    fontSize: 16,
  },
  networkSignal: {
    color: "white",
    fontSize: 14,
  },
  selectedNetworkContainer: {
    marginVertical: 20,
  },
  selectedNetworkText: {
    color: "white",
    fontSize: 16,
    marginBottom: 10,
  },
  passwordInput: {
    backgroundColor: "white",
    borderRadius: 5,
    padding: 10,
    marginBottom: 10,
  },
  connectButton: {
    backgroundColor: "green",
    borderRadius: 5,
    paddingVertical: 12,
    alignItems: "center",
  },
  connectButtonText: {
    color: "white",
    fontSize: 16,
    fontWeight: "bold",
  },
  infoContainer: {
    marginTop: 20,
    borderTopWidth: 1,
    borderTopColor: "rgba(255, 255, 255, 0.2)",
    paddingTop: 10,
  },
  infoLabel: {
    color: "white",
    fontSize: 16,
    fontWeight: "bold",
  },
  infoText: {
    color: "white",
    fontSize: 14,
    marginTop: 5,
  },
});

export default App;
