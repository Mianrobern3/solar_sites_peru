# Solar Sites Peru 🌞

## Descripción
Herramienta de análisis y visualización para identificar sitios potenciales de energía solar en Perú, considerando la ubicación de subestaciones eléctricas y niveles de radiación solar.

## Características 🚀
- Visualización de subestaciones eléctricas (500kV, 220kV, 138kV)
- Mapa de calor de radiación solar
- Identificación de sitios solares potenciales
- Análisis de áreas de cobertura
- Vista satelital integrada
- Interfaz interactiva con controles de capa

## Tecnologías Utilizadas 💻
- Python 3.8+
- Folium (Visualización de mapas)
- NumPy (Análisis numérico)
- Jinja2 (Templates HTML)
- Logging (Registro de eventos)

## Instalación 🛠️
1. Clonar el repositorio:
  bash
  git clone https://github.com/Mianrobern3/solar_sites_peru.git
  cd solar_sites_peru

2. Crear un entorno virtual (opcional pero recomendado):
  bash
  python -m venv venv
  source venv/bin/activate # Linux/Mac
  venv\Scripts\activate # Windows

3. Instalar dependencias:
  bash
  pip install -r requirements.txt

## Estructura del Proyecto 📁
solar_sites_peru/
├── src/
│ ├── templates/ # Templates HTML
│ ├── static/ # Archivos estáticos (CSS)
│ ├── models/ # Modelos de datos y análisis
│ ├── utils/ # Utilidades y helpers
│ ├── config/ # Configuraciones
│ └── main.py # Punto de entrada
├── data/
│ ├── processed/ # Datos procesados
│ └── raw/ # Datos crudos
└── requirements.txt # Dependencias

## Uso 📊
1. Ejecutar el programa:
  bash
  python src/main.py
2. Abrir el mapa generado:
  data/processed/solar_sites_map.html

## Capas Disponibles 🗺️
- **Subestaciones Eléctricas**: Visualización de SET por nivel de voltaje
- **Áreas de Cobertura**: Radio de influencia de 50km para cada SET
- **Sitios Solares**: Ubicaciones potenciales para proyectos solares
- **Mapa de Calor**: Visualización de niveles de radiación solar
- **Vista Satelital**: Imagen satelital del terreno

## Contribución 🤝
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores.

## Licencia 📄
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto 📧
- Desarrollador: [Miguel Angel Rodriguez]
- GitHub: [@Mianrobern3](https://github.com/Mianrobern3)

## Agradecimientos 🙏
- OSINERGMIN
- COES
- Global Solar Atlas
