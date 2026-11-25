# RectangleArea Servisi (ROS 2 Ödev)

Bu repo, ROS 2 üzerinde özel bir servis arayüzü (`RectangleArea.srv`) tanımlayarak dikdörtgen alanı hesaplayan sunucu ve istemci düğümlerini içerir. Bonus olarak yanıta `bool success` alanı eklenmiş ve negatif kenar değerleri reddedilecek şekilde ayarlanmıştır.

## Paket Yapısı

- `alan_interfaces`: `srv/RectangleArea.srv` servis tanımını içerir (`width`, `height` -> `area`, `success`).
- `alan_py`: `alan_sunucu` ve `alan_istemci` Python düğümlerini içerir.

## Kurulum ve Derleme

Paketleri ROS 2 çalışma alanınızın `src` klasörüne kopyalayıp derleyin:

```bash
cp -r alan_interfaces alan_py ~/ros2_ws/src/
cd ~/ros2_ws
colcon build --packages-select alan_interfaces alan_py
source install/setup.bash
```

## Çalıştırma

### 1. Sunucuyu Başlatma

Birinci terminalde:

```bash
source ~/ros2_ws/install/setup.bash
ros2 run alan_py alan_sunucu
```

### 2. İstemci ile Çağrı Yapma

İkinci terminalde (iki sayıyı komut satırından vererek):

```bash
source ~/ros2_ws/install/setup.bash
ros2 run alan_py alan_istemci 5.0 4.0
```

Negatif değer testi (bonus):

```bash
ros2 run alan_py alan_istemci -3.0 4.0
```

## `ros2 service call` ile Doğrulama

Sunucu çalışırken başka bir terminalden doğrudan `ros2 service call` ile de test edilmiştir:

### Geçerli İstek

```bash
$ ros2 service call /rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.5, height: 4.0}"
requester: making request: alan_interfaces.srv.RectangleArea_Request(width=6.5, height=4.0)

response:
alan_interfaces.srv.RectangleArea_Response(area=26.0, success=True)
```

### Negatif Değer Testi (Bonus)

```bash
$ ros2 service call /rectangle_area alan_interfaces/srv/RectangleArea "{width: -5.0, height: 3.0}"
requester: making request: alan_interfaces.srv.RectangleArea_Request(width=-5.0, height=3.0)

response:
alan_interfaces.srv.RectangleArea_Response(area=0.0, success=False)
```
