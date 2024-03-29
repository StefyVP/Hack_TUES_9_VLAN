
![image](https://user-images.githubusercontent.com/78636566/233288078-397bec0b-52ce-4773-91c8-403cc7594865.png)


# Ve-Fi

## След стартиране на приложението, то показва главната си цел, а именно да показва всички налични за свързване в околността Wi-Fi мрежи. При свързване към някоя от тях апликацията ни предоставя информация за мрежата, например колко безопасна и достоверна е тя, както и други ценни и важни функции, свързани с компютърните мрежи и сигурността. Приложението може да се изтегли във формата на desktop приложение и на мобилно приложение.


## Езици

За разработването на Ve-Fi сме използвали:
* Desktop App (Python)
  * sys library
  * pyqt5
  * socket
  * datetime

* Сайт
  * HTML
  * CSS

* Mobile App 
  * React-native
  * @react-native-community/netinfo: за получаване на мрежова информация
  * react-native-wifi-reborn: за управление на Wi-Fi връзки
  * react-native-vector-icons/FontAwesome: за използване на страхотни икони на шрифта
  * react-native-background-timer: за изпълнение на фонови задачи
  * react-native-geolocation-service: за да получите текущото местоположение

## Изтегляне

Има два начина да си изтеглите Ve-Fi:

![image](https://user-images.githubusercontent.com/78636566/233289102-b7d173e7-fefc-4831-80ec-83ba96329bc7.png)

1. При сваляне на git-repository като zip:

- трябва да изтеглите библиотеките - sys, pyqt5, socket, datetime ( pip install *библиотека* )
- стартирате app.py и всичко е готово

2. Може да свалите Ve-Fi и в мобилната му версия:
Това е React Native приложение, което се свързва към избрана Wi-Fi мрежа и след това извършва серия от тестове, за да провери мрежовата връзка. Той използва следните пакети:
 
## Използване

Има два начина да използвате Ve-Fi:

1. В Desktop app - след стартиране има два възможни случая за използване:
- пуснали сте го докато сте били свързани към мрежа: тогава можете веднага да проверите колко е безопасна тази мрежа с предназначените бутони
- пуснали сте го докато НЕ сте били свързани към мрежа: тогава избирате мрежата, към която искате да свържете от scroll-bar-a и въвеждате паролата й;
След това първото тире се повтаря;

2. В Mobile app

Когато приложението се стартира, то извлича наличните Wi-Fi мрежи и ги показва в списък. Когато потребителят избере мрежа и въведе парола, приложението се опитва да се свърже с мрежата. Ако връзката е успешна, приложението започва да извършва серия от тестове, за да провери мрежовата връзка.

Тестовете включват:

1) Проверка на ping свързаността
2) Проверка на DNS spoofing
3) Взимане на текущото местоположение
4) Получаване на времето за връзка

Приложението показва резултатите от тези тестове в реално време. То също така периодично извършва тези тестове във фонов режим и актуализира резултатите, ако се променят.

## "Готвачите"

* Боян Жечев 10 г - mobile app, мрежи
* Ростислав Ангелов 10 г - mobile app
* Николай Захариев 10 а - design, logo
* Иоан Евгениев 10 г - site, video
* Елена Чернева 10 г - desktop app, design

**Линк към презентацията: https://docs.google.com/presentation/d/1pxFwEmfCwoBZ6kjgL9Zd0_c2npJ918jDPXufHTlnnlY/edit?usp=sharing
