# simsar-air-defense
## air_defense_system/
│
├── config/
│   ├── settings.yaml           # Genel ayarlar
│   ├── color_rules.yaml        # Renk → IFF kuralları
│   └── targets.yaml            # Cisim türleri ve özellikleri
│
├── core/
│   ├── __init__.py
│   ├── pipeline.py             # Ana işlem hattı
│   └── context.py              # Paylaşılan veri yapısı
│
├── detection/
│   ├── __init__.py
│   ├── base_detector.py        # Soyut detector
│   ├── yolo_detector.py        # YOLO implementasyonu
│   └── aircraft_classifier.py  # F16/drone/kuş sınıflandırma
│
├── identification/
│   ├── __init__.py
│   ├── base_identifier.py      # Soyut IFF
│   ├── color_identifier.py     # Renk tabanlı dost/düşman
│   └── iff_rules.py            # Kural tanımları
│
├── targeting/
│   ├── __init__.py
│   ├── base_target_calc.py     # Soyut hedef hesaplayıcı
│   ├── balloon_target.py       # Balon pozisyon hesabı
│   └── offset_calculator.py    # Cisim → Balon offset
│
├── control/
│   ├── __init__.py
│   ├── base_controller.py      # Soyut kontrolcü
│   ├── pid_controller.py       # PID implementasyonu
│   └── motor_driver.py         # Motor haberleşme
│
├── decision/
│   ├── __init__.py
│   ├── base_decision.py        # Soyut karar verici
│   ├── engagement_rules.py     # Angajman kuralları
│   └── threat_evaluator.py     # Tehdit değerlendirme
│
├── interfaces/
│   ├── __init__.py
│   ├── i_detector.py
│   ├── i_identifier.py
│   ├── i_target_calculator.py
│   ├── i_controller.py
│   └── i_decision_maker.py
│
├── models/
│   ├── __init__.py
│   ├── aircraft.py             # Cisim veri modeli
│   ├── target.py               # Hedef veri modeli
│   └── engagement.py           # Angajman veri modeli
│
├── utils/
│   ├── __init__.py
│   ├── color_utils.py          # Renk analiz yardımcıları
│   ├── geometry.py             # Geometri hesaplamaları
│   └── logger.py
│
├── tests/
│   ├── test_color_identifier.py
│   ├── test_balloon_target.py
│   └── test_engagement_rules.py
│
└── main.py
