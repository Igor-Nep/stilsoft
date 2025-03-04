
media-server            | 2024-11-01T11:39:35.628789Z DEBUG media_server_webrtc::session: 222: Состояние ICE Connection: 'state: 'connected', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '9267b139-c53f-4373-944c-fb25b579d696''


media-server            | 2024-11-01T11:39:35.837159Z DEBUG media_server_webrtc::session: 235: Состояние Peer Connection: 'state: 'connected', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '9267b139-c53f-4373-944c-fb25b579d696''


media-server            | 2024-11-01T11:39:35.838077Z DEBUG media_server_webrtc::media_encoding: 49: Запущена таска обслуживающая кодирование медиа для потребителя webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session_id: '9267b139-c53f-4373-944c-fb25b579d696''


media-server            | 2024-11-01T11:40:11.749980Z DEBUG media_server_webrtc::session: 47: Завершена таска обслуживающая сессию webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '9267b139-c53f-4373-944c-fb25b579d696''


media-server            | 2024-11-01T11:40:11.750021Z DEBUG media_server_webrtc::server: 196: Завершена работа сессии webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '9267b139-c53f-4373-944c-fb25b579d696''


media-server            | 2024-11-01T11:40:11.750741Z ERROR media_server_webrtc::signalling: 214: Сигнальный сервер прислал сообщение об ошибке: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', err: 'Session 9267b139-c53f-4373-944c-fb25b579d696 doesn't exist''


media-server            | 2024-11-01T11:40:11.754991Z DEBUG media_server_webrtc::session: 235: Состояние Peer Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '9267b139-c53f-4373-944c-fb25b579d696''


media-server            | 2024-11-01T11:40:11.757581Z DEBUG media_server_webrtc::session: 222: Состояние ICE Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '9267b139-c53f-4373-944c-fb25b579d696''


media-server            | 2024-11-01T11:40:11.776380Z DEBUG media_server_webrtc::media_encoding: 54: Завершена таска обслуживающая кодирование медиа для потребителя webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session_id: '9267b139-c53f-4373-944c-fb25b579d696''


media-server            | 2024-11-01T11:48:02.384302Z DEBUG media_server::new_pipeline::controller: 462: Завершен таск SourcePipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T11:48:02.547393Z DEBUG media_server::new_pipeline::controller: 335: Таск SourcePipeline был закрыт: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T11:48:02.547493Z DEBUG media_server_webrtc::server: 44: Завершена таска обслуживающая сервер webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T11:48:02.547503Z ERROR media_server::server_task: 460: Pipeline прислал событие об ошибке: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://192.168.202.9:44359/rtsp_stream', Error: 'Вышел timeout прихода кадров''


media-server            | 2024-11-01T11:48:02.547603Z DEBUG media_server_webrtc::signalling: 32: Завершена таска обслуживающая взаимодействие с сигнальным сервером: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T11:48:02.548808Z DEBUG media_server_webrtc::session: 47: Завершена таска обслуживающая сессию webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'd83a7d6b-f1cc-4e92-bba5-20f2f387994c''


media-server            | 2024-11-01T11:48:02.549020Z DEBUG media_server_webrtc::session: 47: Завершена таска обслуживающая сессию webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'c08090b3-ef2a-43f8-81fa-606f0daab54c''


media-server            | 2024-11-01T11:48:02.549522Z DEBUG media_server_webrtc::session: 47: Завершена таска обслуживающая сессию webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '210109c6-c181-4e59-b6fc-c2f1ea0bc07b''


media-server            | 2024-11-01T11:48:02.550163Z DEBUG media_server_webrtc::session: 47: Завершена таска обслуживающая сессию webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '28adec0d-8be1-40f7-9402-06b695433f78''


media-server            | 2024-11-01T11:48:02.551417Z DEBUG media_server_webrtc::session: 47: Завершена таска обслуживающая сессию webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'd522b678-0f1a-40f7-8e31-cb095f69ad24''


media-server            | 2024-11-01T11:48:02.552968Z DEBUG media_server_webrtc::session: 47: Завершена таска обслуживающая сессию webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'e111c3e1-b7a4-49ff-ac54-695591a7ec05''


media-server            | 2024-11-01T11:48:02.553344Z DEBUG media_server_webrtc::session: 222: Состояние ICE Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'd83a7d6b-f1cc-4e92-bba5-20f2f387994c''


media-server            | 2024-11-01T11:48:02.553531Z DEBUG media_server_webrtc::session: 235: Состояние Peer Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'd83a7d6b-f1cc-4e92-bba5-20f2f387994c''


media-server            | 2024-11-01T11:48:02.555534Z DEBUG media_server_webrtc::session: 235: Состояние Peer Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'c08090b3-ef2a-43f8-81fa-606f0daab54c''


media-server            | 2024-11-01T11:48:02.556284Z DEBUG media_server_webrtc::session: 222: Состояние ICE Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'c08090b3-ef2a-43f8-81fa-606f0daab54c''


media-server            | 2024-11-01T11:48:02.557009Z DEBUG media_server_webrtc::session: 235: Состояние Peer Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'd522b678-0f1a-40f7-8e31-cb095f69ad24''


media-server            | 2024-11-01T11:48:02.557933Z DEBUG media_server_webrtc::session: 235: Состояние Peer Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '210109c6-c181-4e59-b6fc-c2f1ea0bc07b''


media-server            | 2024-11-01T11:48:02.558122Z DEBUG media_server_webrtc::session: 222: Состояние ICE Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '210109c6-c181-4e59-b6fc-c2f1ea0bc07b''


media-server            | 2024-11-01T11:48:02.560428Z DEBUG media_server_webrtc::session: 222: Состояние ICE Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '28adec0d-8be1-40f7-9402-06b695433f78''


media-server            | 2024-11-01T11:48:02.562513Z DEBUG media_server_webrtc::session: 235: Состояние Peer Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'e111c3e1-b7a4-49ff-ac54-695591a7ec05''


media-server            | 2024-11-01T11:48:02.562941Z DEBUG media_server_webrtc::session: 235: Состояние Peer Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '28adec0d-8be1-40f7-9402-06b695433f78''


media-server            | 2024-11-01T11:48:02.564288Z DEBUG media_server_webrtc::session: 222: Состояние ICE Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'e111c3e1-b7a4-49ff-ac54-695591a7ec05''


media-server            | 2024-11-01T11:48:02.557259Z DEBUG media_server_webrtc::session: 222: Состояние ICE Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: 'd522b678-0f1a-40f7-8e31-cb095f69ad24''


media-server            | 2024-11-01T11:48:02.566543Z DEBUG media_server_webrtc::session: 235: Состояние Peer Connection: 'state: 'closed', vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session: '28adec0d-8be1-40f7-9402-06b695433f78''


media-server            | 2024-11-01T11:48:02.609590Z DEBUG media_server_webrtc::media_encoding: 54: Завершена таска обслуживающая кодирование медиа для потребителя webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session_id: 'c08090b3-ef2a-43f8-81fa-606f0daab54c''


media-server            | 2024-11-01T11:48:02.609825Z DEBUG media_server_webrtc::media_encoding: 54: Завершена таска обслуживающая кодирование медиа для потребителя webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session_id: '210109c6-c181-4e59-b6fc-c2f1ea0bc07b''


media-server            | 2024-11-01T11:48:02.610678Z DEBUG media_server_webrtc::media_encoding: 54: Завершена таска обслуживающая кодирование медиа для потребителя webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session_id: 'd83a7d6b-f1cc-4e92-bba5-20f2f387994c''


media-server            | 2024-11-01T11:48:02.611429Z DEBUG media_server_webrtc::media_encoding: 54: Завершена таска обслуживающая кодирование медиа для потребителя webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session_id: '28adec0d-8be1-40f7-9402-06b695433f78''


media-server            | 2024-11-01T11:48:02.615790Z DEBUG media_server_webrtc::media_encoding: 54: Завершена таска обслуживающая кодирование медиа для потребителя webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session_id: 'd522b678-0f1a-40f7-8e31-cb095f69ad24''


media-server            | 2024-11-01T11:48:02.620877Z DEBUG media_server_webrtc::media_encoding: 54: Завершена таска обслуживающая кодирование медиа для потребителя webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', session_id: 'e111c3e1-b7a4-49ff-ac54-695591a7ec05''


media-server            | 2024-11-01T11:48:13.100797Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:48:13.100952Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:48:33.106735Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:48:33.106779Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:48:33.106993Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000069266''


media-server            | 2024-11-01T11:48:43.125369Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:48:43.125651Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:48:43.125907Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000497262''


media-server            | 2024-11-01T11:48:43.502651Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:48:43.502962Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.401903919''


media-server            | 2024-11-01T11:48:53.149799Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:48:53.150148Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:49:13.152620Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:49:13.152730Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:49:13.153145Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000514249''


media-server            | 2024-11-01T11:49:23.177237Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:49:23.177274Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:49:23.177732Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000060194''


media-server            | 2024-11-01T11:49:23.514974Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:49:23.515241Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.365430311''


media-server            | 2024-11-01T11:49:33.197729Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:49:33.198283Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:49:53.202868Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:49:53.203328Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:49:53.203518Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000501587''


media-server            | 2024-11-01T11:50:03.223487Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:50:03.223532Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:50:03.223664Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000088785''


media-server            | 2024-11-01T11:50:03.574231Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:50:03.575134Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.376549843''


media-server            | 2024-11-01T11:50:13.238439Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:50:13.238971Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:50:33.241514Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:50:33.241572Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:50:33.241763Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000120979''


media-server            | 2024-11-01T11:50:33.737631Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:50:33.737910Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'Ошибка pipeline во время его запуска: 'Could not read from resource.'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '20.499447689''


media-server            | 2024-11-01T11:50:43.263298Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:50:43.263540Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:51:03.265713Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:51:03.265770Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:51:03.265818Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000096386''


media-server            | 2024-11-01T11:51:13.292678Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:51:13.292717Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:51:13.292764Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000080467''


media-server            | 2024-11-01T11:51:13.684838Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:51:13.685006Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.421665495''


media-server            | 2024-11-01T11:51:23.306322Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:51:23.306639Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:51:43.315890Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:51:43.316325Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:51:43.316633Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000501841''


media-server            | 2024-11-01T11:51:53.367569Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:51:53.368104Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:51:53.368422Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000708111''


media-server            | 2024-11-01T11:51:53.705562Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:51:53.705715Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.39929455''


media-server            | 2024-11-01T11:52:03.385813Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:52:03.386339Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:52:23.392697Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:52:23.392816Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:52:23.393181Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00015681''


media-server            | 2024-11-01T11:52:33.415047Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:52:33.415085Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:52:33.415248Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000057013''


media-server            | 2024-11-01T11:52:33.761819Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:52:33.762084Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.376046991''


media-server            | 2024-11-01T11:52:43.433766Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:52:43.434172Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:53:03.433330Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:53:03.433434Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:53:03.433501Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000151646''


media-server            | 2024-11-01T11:53:13.462614Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:53:13.462950Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:53:13.463258Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000413449''


media-server            | 2024-11-01T11:53:13.787883Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:53:13.788351Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.354216956''


media-server            | 2024-11-01T11:53:23.483121Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:53:23.483326Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:53:43.498596Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:53:43.499203Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:53:43.499954Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000948951''


media-server            | 2024-11-01T11:53:53.516086Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:53:53.516132Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:53:53.516157Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000066421''


media-server            | 2024-11-01T11:53:53.862593Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:53:53.862897Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.379762944''


media-server            | 2024-11-01T11:54:03.541501Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:54:03.541583Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:54:23.538034Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:54:23.538083Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:54:23.538257Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000094813''


media-server            | 2024-11-01T11:54:33.553749Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:54:33.553800Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:54:33.553987Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000090805''


media-server            | 2024-11-01T11:54:33.913276Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:54:33.913418Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.371895932''


media-server            | 2024-11-01T11:54:43.572453Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:54:43.572955Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:55:03.579562Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:55:03.579605Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:55:03.580297Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000071603''


media-server            | 2024-11-01T11:55:13.600597Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:55:13.600634Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:55:13.600874Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000058534''


media-server            | 2024-11-01T11:55:13.993512Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:55:13.993978Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.421101598''


media-server            | 2024-11-01T11:55:23.618901Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:55:23.619267Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:55:43.620129Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:55:43.620221Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:55:43.620266Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000129082''


media-server            | 2024-11-01T11:55:53.637769Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:55:53.637823Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:55:53.639845Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000103571''


media-server            | 2024-11-01T11:55:54.052970Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:55:54.053032Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.434110005''


media-server            | 2024-11-01T11:56:03.661121Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:56:03.661440Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:56:23.665672Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:56:23.665988Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:56:23.666061Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000366741''


media-server            | 2024-11-01T11:56:33.698945Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:56:33.699410Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:56:33.699521Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000531337''


media-server            | 2024-11-01T11:56:34.089409Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:56:34.089470Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.428338909''


media-server            | 2024-11-01T11:56:43.728887Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:56:43.729059Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:57:03.729838Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:57:03.729871Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:57:03.730102Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000052894''


media-server            | 2024-11-01T11:57:13.747432Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:57:13.747469Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:57:13.747568Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000057512''


media-server            | 2024-11-01T11:57:14.095295Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:57:14.095509Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.366586614''


media-server            | 2024-11-01T11:57:23.770858Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:57:23.772796Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:57:43.767235Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:57:43.767429Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:57:43.767665Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00031302''


media-server            | 2024-11-01T11:57:53.778386Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:57:53.778426Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:57:53.778492Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000058848''


media-server            | 2024-11-01T11:57:54.040074Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:57:54.040197Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.269270651''


media-server            | 2024-11-01T11:58:03.785000Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:58:03.785113Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:58:23.788694Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:58:23.788736Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:58:23.788836Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000072178''


media-server            | 2024-11-01T11:58:33.797135Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:58:33.797176Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:58:33.797245Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000065531''


media-server            | 2024-11-01T11:58:33.845533Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:58:33.845592Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.060580498''


media-server            | 2024-11-01T11:58:43.804138Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:58:43.804249Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:59:03.804874Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:59:03.804908Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:59:03.804926Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000049175''


media-server            | 2024-11-01T11:59:13.812262Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:59:13.812308Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:59:13.812455Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00006764''


media-server            | 2024-11-01T11:59:13.866328Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:59:13.866412Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.06222908''


media-server            | 2024-11-01T11:59:23.822539Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:59:23.822649Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:59:43.827634Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:59:43.827674Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:59:43.827752Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000065235''


media-server            | 2024-11-01T11:59:53.836200Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T11:59:53.836233Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T11:59:53.836300Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000054534''


media-server            | 2024-11-01T11:59:53.904961Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T11:59:53.905067Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.082473621''


media-server            | 2024-11-01T12:00:03.842713Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:00:03.842831Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:00:23.847127Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:00:23.847184Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:00:23.847317Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000092607''


media-server            | 2024-11-01T12:00:33.857254Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:00:33.857304Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:00:33.857439Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000090777''


media-server            | 2024-11-01T12:00:33.942680Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:00:33.942823Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.100015077''


media-server            | 2024-11-01T12:00:43.866725Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:00:43.866889Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:01:03.869809Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:01:03.869845Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:01:03.869919Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000053905''


media-server            | 2024-11-01T12:01:13.876384Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:01:13.876418Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:01:13.876491Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000058941''


media-server            | 2024-11-01T12:01:13.997858Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:01:13.997912Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.131182735''


media-server            | 2024-11-01T12:01:23.882428Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:01:23.882465Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:01:43.884044Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:01:43.884075Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:01:43.884091Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000044075''


media-server            | 2024-11-01T12:01:53.888363Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:01:53.888390Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:01:53.888407Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000039344''


media-server            | 2024-11-01T12:01:53.914211Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:01:53.914247Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.031814766''


media-server            | 2024-11-01T12:02:03.892810Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:02:03.892912Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:02:23.893953Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:02:23.893985Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:02:23.894005Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000048823''


media-server            | 2024-11-01T12:02:33.898404Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:02:33.898442Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:02:33.898463Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000054068''


media-server            | 2024-11-01T12:02:33.917290Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:02:33.917338Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.024523507''


media-server            | 2024-11-01T12:02:43.903322Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:02:43.903362Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:03:03.905282Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:03:03.905317Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:03:03.905340Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000051665''


media-server            | 2024-11-01T12:03:13.910744Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:03:13.910771Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:03:13.910788Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000040633''


media-server            | 2024-11-01T12:03:13.922272Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:03:13.922349Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.01898172''


media-server            | 2024-11-01T12:03:23.915393Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:03:23.915461Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:03:43.916500Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:03:43.916528Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:03:43.916544Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000040281''


media-server            | 2024-11-01T12:03:53.920215Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:03:53.920245Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:03:53.920263Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000053119''


media-server            | 2024-11-01T12:03:53.931740Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:03:53.931784Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.016385883''


media-server            | 2024-11-01T12:04:03.925618Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:04:03.925658Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:04:23.927404Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:04:23.927447Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:04:23.927469Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000059223''


media-server            | 2024-11-01T12:04:33.933538Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:04:33.933581Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:04:33.933652Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000070109''


media-server            | 2024-11-01T12:04:33.948917Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:04:33.948973Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.023346566''


media-server            | 2024-11-01T12:04:43.938946Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:04:43.938993Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:05:03.941512Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:05:03.941543Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:05:03.941598Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000054785''


media-server            | 2024-11-01T12:05:13.946421Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:05:13.946461Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:05:13.946483Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000057059''


media-server            | 2024-11-01T12:05:13.960610Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:05:13.960648Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.021698429''


media-server            | 2024-11-01T12:05:23.951324Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:05:23.951374Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:05:43.952612Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:05:43.952637Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:05:43.952654Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000037404''


media-server            | 2024-11-01T12:05:53.957101Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:05:53.957137Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:05:53.957170Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00005321''


media-server            | 2024-11-01T12:05:53.964490Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:05:53.964531Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.013200977''


media-server            | 2024-11-01T12:06:03.961729Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:06:03.961780Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:06:23.963986Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:06:23.964014Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:06:23.964031Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000041642''


media-server            | 2024-11-01T12:06:33.968853Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:06:33.968888Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:06:33.968908Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000048526''


media-server            | 2024-11-01T12:06:33.987229Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:06:33.987287Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.025551137''


media-server            | 2024-11-01T12:06:43.974233Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:06:43.974275Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:07:03.977586Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:07:03.977618Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:07:03.977639Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000047617''


media-server            | 2024-11-01T12:07:13.982389Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:07:13.982427Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:07:13.982447Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000057878''


media-server            | 2024-11-01T12:07:13.995836Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:07:13.995874Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.02163627''


media-server            | 2024-11-01T12:07:23.987011Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:07:23.987061Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:07:43.990480Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:07:43.990508Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:07:43.990526Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000041767''


media-server            | 2024-11-01T12:07:53.995204Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:07:53.995233Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:07:53.995251Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000041491''


media-server            | 2024-11-01T12:07:53.999492Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:07:53.999540Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.01252311''


media-server            | 2024-11-01T12:08:03.998831Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:08:03.998877Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:08:24.000949Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:08:24.000983Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:08:24.000999Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000047874''


media-server            | 2024-11-01T12:08:34.005040Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:08:34.005073Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:08:34.005093Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000049185''


media-server            | 2024-11-01T12:08:34.026842Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:08:34.026880Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.028043176''


media-server            | 2024-11-01T12:08:44.008952Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:08:44.009004Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:09:04.011807Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:09:04.011839Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:09:04.011857Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000047219''


media-server            | 2024-11-01T12:09:14.016379Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:09:14.016408Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:09:14.016443Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000047268''


media-server            | 2024-11-01T12:09:14.030749Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:09:14.030798Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.021841642''


media-server            | 2024-11-01T12:09:24.020770Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:09:24.020808Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:09:44.023208Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:09:44.023237Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:09:44.023255Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000041246''


media-server            | 2024-11-01T12:09:54.027111Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:09:54.027147Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:09:54.027168Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000052554''


media-server            | 2024-11-01T12:09:54.033102Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:09:54.033137Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.012362461''


media-server            | 2024-11-01T12:10:04.031251Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:10:04.031292Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:10:24.033605Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:10:24.033632Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:10:24.033652Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000042767''


media-server            | 2024-11-01T12:10:34.037668Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:10:34.037701Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:10:34.037733Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000060793''


media-server            | 2024-11-01T12:10:34.043777Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:10:34.043817Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.012561709''


media-server            | 2024-11-01T12:10:44.041712Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:10:44.041756Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:11:04.044236Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:11:04.044267Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:11:04.044284Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000044442''


media-server            | 2024-11-01T12:11:14.048050Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:11:14.048079Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:11:14.048094Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.0000412''


media-server            | 2024-11-01T12:11:14.055111Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:11:14.055153Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.013438438''


media-server            | 2024-11-01T12:11:24.051966Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:11:24.052013Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:11:44.054498Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:11:44.054527Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:11:44.054545Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000042395''


media-server            | 2024-11-01T12:11:54.059479Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:11:54.059507Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:11:54.059524Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000040512''


media-server            | 2024-11-01T12:11:54.063031Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:11:54.063068Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.011099292''


media-server            | 2024-11-01T12:12:04.064347Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:12:04.064453Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:12:24.065918Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:12:24.065948Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:12:24.065965Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000043735''


media-server            | 2024-11-01T12:12:34.070550Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:12:34.070577Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:12:34.070597Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000042793''


media-server            | 2024-11-01T12:12:34.080825Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:12:34.080861Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.016511422''


media-server            | 2024-11-01T12:12:44.074945Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:12:44.074980Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:13:04.076641Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:13:04.076689Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:13:04.076707Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000062932''


media-server            | 2024-11-01T12:13:14.080761Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:13:14.080790Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:13:14.080807Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000043489''


media-server            | 2024-11-01T12:13:14.089083Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:13:14.089151Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.014175087''


media-server            | 2024-11-01T12:13:24.084823Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:13:24.084861Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:13:44.087015Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:13:44.087051Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:13:44.087073Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000051933''


media-server            | 2024-11-01T12:13:54.092536Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:13:54.092573Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:13:54.092619Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000057891''


media-server            | 2024-11-01T12:13:54.100169Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:13:54.100210Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.015381928''


media-server            | 2024-11-01T12:14:04.099042Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:14:04.099123Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:14:24.101127Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:14:24.101157Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:14:24.101173Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00004219''


media-server            | 2024-11-01T12:14:34.105328Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:14:34.105355Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:14:34.105372Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00004014''


media-server            | 2024-11-01T12:14:34.116655Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:14:34.116712Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.017666474''


media-server            | 2024-11-01T12:14:44.108878Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:14:44.108920Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:15:04.110762Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:15:04.110790Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:15:04.110807Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000040013''


media-server            | 2024-11-01T12:15:14.115637Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:15:14.115666Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:15:14.115682Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000043283''


media-server            | 2024-11-01T12:15:14.124368Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:15:14.124416Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.015530472''


media-server            | 2024-11-01T12:15:24.120289Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:15:24.120325Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:15:44.121758Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:15:44.121803Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:15:44.121825Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000061931''


media-server            | 2024-11-01T12:15:54.126568Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:15:54.126600Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:15:54.126644Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000047561''


media-server            | 2024-11-01T12:15:54.135880Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:15:54.135917Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.015624023''


media-server            | 2024-11-01T12:16:04.131719Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:16:04.131806Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:16:24.133308Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:16:24.133338Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:16:24.133398Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000047671''


media-server            | 2024-11-01T12:16:34.137542Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:16:34.137570Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:16:34.137590Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00004419''


media-server            | 2024-11-01T12:16:34.158604Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:16:34.158640Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.026917115''


media-server            | 2024-11-01T12:16:44.142707Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:16:44.142747Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:17:04.144491Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:17:04.144526Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:17:04.144548Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000053562''


media-server            | 2024-11-01T12:17:14.149116Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:17:14.149147Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:17:14.149169Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000046691''


media-server            | 2024-11-01T12:17:14.162120Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:17:14.162154Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.019443708''


media-server            | 2024-11-01T12:17:24.152799Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:17:24.152838Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:17:44.155702Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:17:44.155731Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:17:44.155748Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000044006''


media-server            | 2024-11-01T12:17:54.161603Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:17:54.161637Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:17:54.161686Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000060069''


media-server            | 2024-11-01T12:17:54.172711Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:17:54.172754Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.019949053''


media-server            | 2024-11-01T12:18:04.166921Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:18:04.166960Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:18:24.169819Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:18:24.169857Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:18:24.169902Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000053584''


media-server            | 2024-11-01T12:18:34.174872Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:18:34.174906Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:18:34.174930Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000052923''


media-server            | 2024-11-01T12:18:34.195166Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:18:34.195211Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.028284516''


media-server            | 2024-11-01T12:18:44.180251Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:18:44.180328Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:19:04.181394Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:19:04.181422Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:19:04.181439Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000040817''


media-server            | 2024-11-01T12:19:14.185187Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:19:14.185224Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:19:14.185246Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000054337''


media-server            | 2024-11-01T12:19:14.198287Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:19:14.198327Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.018072527''


media-server            | 2024-11-01T12:19:24.188607Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:19:24.188675Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:19:44.190846Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:19:44.190877Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:19:44.190895Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000044313''


media-server            | 2024-11-01T12:19:54.196850Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:19:54.196889Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:19:54.196943Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000059166''


media-server            | 2024-11-01T12:19:54.207905Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:19:54.207941Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.019331848''


media-server            | 2024-11-01T12:20:04.201821Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:20:04.201859Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:20:24.204003Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:20:24.204032Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:20:24.204050Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000042323''


media-server            | 2024-11-01T12:20:34.208506Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:20:34.208533Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:20:34.208549Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000041014''


media-server            | 2024-11-01T12:20:34.234737Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:20:34.234790Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.03295121''


media-server            | 2024-11-01T12:20:44.214500Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:20:44.214619Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:21:04.217779Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:21:04.217818Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:21:04.217849Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000057905''


media-server            | 2024-11-01T12:21:14.223456Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:21:14.223485Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:21:14.223501Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000040751''


media-server            | 2024-11-01T12:21:14.235886Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:21:14.235924Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.021427111''


media-server            | 2024-11-01T12:21:24.227776Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:21:24.227817Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:21:44.230025Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:21:44.230060Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:21:44.230082Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00005299''


media-server            | 2024-11-01T12:21:52.229949Z DEBUG media_server::new_pipeline::controller: 459: Запущен таск SourcePipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T12:21:52.229949Z  INFO media_server::server_task: 506: Успешно создан pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://192.168.202.9:44359/rtsp_stream''


media-server            | 2024-11-01T12:21:52.230012Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:21:52.230024Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'ok', 'Duration: '28.00224644''


media-server            | 2024-11-01T12:21:52.230087Z DEBUG media_server_webrtc::server: 39: Запущена таска обслуживающая сервер webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T12:21:52.230121Z DEBUG media_server_webrtc::signalling: 26: Запущена таска обслуживающая взаимодействие с сигнальным сервером: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T12:21:54.234526Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:21:54.234565Z  INFO media_server::server_task: 306: Остановка старого pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:21:54.234886Z DEBUG media_server::new_pipeline::controller: 462: Завершен таск SourcePipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T12:21:54.241275Z DEBUG media_server::new_pipeline::controller: 335: Таск SourcePipeline был закрыт: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T12:21:54.241337Z  INFO media_server::server_task: 333: Остановлен старый pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:21:54.241354Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:21:54.241364Z DEBUG media_server_webrtc::server: 44: Завершена таска обслуживающая сервер webrtc: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T12:21:54.241447Z DEBUG media_server_webrtc::signalling: 32: Завершена таска обслуживающая взаимодействие с сигнальным сервером: 'vs: '9451284b-149c-4c67-a4bf-8bd0b9244b2e''


media-server            | 2024-11-01T12:22:14.236090Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:22:14.236120Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:22:14.236138Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000043352''


media-server            | 2024-11-01T12:22:24.240303Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:22:24.240334Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:22:24.240352Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00004576''


media-server            | 2024-11-01T12:22:24.264681Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:22:24.264726Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.030194721''


media-server            | 2024-11-01T12:22:34.244408Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:22:34.244450Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:22:54.247110Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:22:54.247140Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:22:54.247157Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000042146''


media-server            | 2024-11-01T12:23:04.251496Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:23:04.251530Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:23:04.251549Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000049745''


media-server            | 2024-11-01T12:23:04.257531Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:23:04.257564Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.013151558''


media-server            | 2024-11-01T12:23:14.256426Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:23:14.256466Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:23:34.257680Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:23:34.257709Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:23:34.257729Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000044547''


media-server            | 2024-11-01T12:23:44.262413Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:23:44.262441Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:23:44.262458Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000040858''


media-server            | 2024-11-01T12:23:44.279747Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:23:44.279814Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.02335594''


media-server            | 2024-11-01T12:23:54.265651Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:23:54.265706Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:24:14.268693Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:24:14.268721Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:24:14.268760Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000046175''


media-server            | 2024-11-01T12:24:24.273657Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:24:24.273686Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:24:24.273719Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00004649''


media-server            | 2024-11-01T12:24:24.279682Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:24:24.279745Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.014086397''


media-server            | 2024-11-01T12:24:34.280506Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:24:34.280583Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:24:54.280400Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:24:54.280435Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:24:54.280456Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000051506''


media-server            | 2024-11-01T12:25:04.284731Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:25:04.284761Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:25:04.284777Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000042735''


media-server            | 2024-11-01T12:25:04.309783Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:25:04.309823Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.029314407''


media-server            | 2024-11-01T12:25:14.289020Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:25:14.289059Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:25:34.290744Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:25:34.290776Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:25:34.290797Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000047504''


media-server            | 2024-11-01T12:25:44.294790Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:25:44.294839Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:25:44.294866Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00007132''


media-server            | 2024-11-01T12:25:44.306846Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:25:44.306899Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.017859079''


media-server            | 2024-11-01T12:25:54.299901Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:25:54.299958Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:26:14.301146Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:26:14.301174Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:26:14.301191Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000040702''


media-server            | 2024-11-01T12:26:24.306084Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:26:24.306124Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:26:24.306195Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.00006904''


media-server            | 2024-11-01T12:26:24.321498Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:26:24.321536Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.021632098''


media-server            | 2024-11-01T12:26:34.312079Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:26:34.312173Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:26:54.314022Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:26:54.314052Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:26:54.314091Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000046667''


media-server            | 2024-11-01T12:27:04.318647Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:27:04.318683Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:27:04.318703Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000053171''


media-server            | 2024-11-01T12:27:04.332892Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:27:04.332931Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.02084629''


media-server            | 2024-11-01T12:27:14.322564Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:27:14.322601Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:27:34.326412Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:27:34.326442Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:27:34.326459Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000042264''


media-server            | 2024-11-01T12:27:44.330521Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:27:44.330559Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:27:44.330579Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000053862''


media-server            | 2024-11-01T12:27:44.335502Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:27:44.335536Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.012967942''


media-server            | 2024-11-01T12:27:54.336621Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:27:54.336739Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:28:14.338041Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:28:14.338075Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:28:14.338093Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000047927''


media-server            | 2024-11-01T12:28:24.342277Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:28:24.342326Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:28:24.342348Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000069618''


media-server            | 2024-11-01T12:28:24.365285Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:28:24.365325Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.02870035''


media-server            | 2024-11-01T12:28:34.346992Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:28:34.347032Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:28:54.349092Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:28:54.349122Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:28:54.349139Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000043219''


media-server            | 2024-11-01T12:29:04.353193Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:29:04.353223Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:29:04.353240Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000042444''


media-server            | 2024-11-01T12:29:04.398143Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:29:04.398188Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.05118968''


media-server            | 2024-11-01T12:29:14.357932Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:29:14.358027Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:29:34.359924Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:29:34.359959Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:29:34.359979Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000051488''


media-server            | 2024-11-01T12:29:44.365011Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:29:44.365044Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:29:44.365093Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000046674''


media-server            | 2024-11-01T12:29:44.378496Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:29:44.378531Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.020596234''


media-server            | 2024-11-01T12:29:54.370245Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:29:54.370285Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:30:14.372191Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:30:14.372223Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:30:14.372242Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000048363''


media-server            | 2024-11-01T12:30:24.375984Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:30:24.376012Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:30:24.376030Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000041622''


media-server            | 2024-11-01T12:30:24.381204Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:30:24.381235Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.010986179''


media-server            | 2024-11-01T12:30:34.381471Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:30:34.381550Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:30:54.382528Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:30:54.382554Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:30:54.382571Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000037969''


media-server            | 2024-11-01T12:31:04.389261Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:31:04.389289Z  WARN media_server::server_task: 248: Отброшен запрос на регистрацию видеоисточника, так как уже существует запущенный процесс регистрации: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'


media-server            | 2024-11-01T12:31:04.389306Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Уже существует запущенный процесс регистрации видеоисточника', 'Duration: '0.000040855''


media-server            | 2024-11-01T12:31:04.404686Z DEBUG media_server::server_task: 299: Удален процесс регистрации для 9451284b-149c-4c67-a4bf-8bd0b9244b2e


media-server            | 2024-11-01T12:31:04.404726Z DEBUG media_server::server_task: 551: Завершена обработка запроса на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', Res: 'Не удалось запустить pipeline в автоматическом режиме выбора транспорта: '["transport: 'Udp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''", "transport: 'Tcp', err: 'pipeline не запущен: 'вышел timeout: startup_timeout: '15 сек'''"]'', 'Duration: '30.023250385''


media-server            | 2024-11-01T12:31:14.393113Z DEBUG media_server::server_task: 237: Пришел запрос на регистрацию видеоисточника: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream', 'Protocol: 'None''


media-server            | 2024-11-01T12:31:14.393149Z  INFO media_server::server_task: 341: Обработка создания нового pipeline: 'Uuid: '9451284b-149c-4c67-a4bf-8bd0b9244b2e', Interfaces: '[192.168.202.9, 172.18.18.123, 172.16.16.124, 10.201.0.1, 10.202.0.1, 10.200.0.1]', Url: 'rtsp://0.0.0.0:44359/rtsp_stream'

