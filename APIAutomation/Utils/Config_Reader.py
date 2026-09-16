import os

class ConfigReader:
    _properties = {}
    # Locates the properties resource file matching your Java architecture layout paths
    _file_path = os.path.join(os.path.dirname(__file__), "..", "resources", "config.properties")

    @classmethod
    def _load_properties(cls):
        if not cls._properties and os.path.exists(cls._file_path):
            try:
                with open(cls._file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        # Skip empty spaces or comment parameters line markings cleanly
                        if line and not line.startswith(("#", ";")) and "=" in line:
                            key, value = line.split("=", 1)
                            cls._properties[key.strip()] = value.strip()
            except Exception as e:
                print(f"[CONFIG ERROR] Failed loading config.properties metadata: {e}")

    @classmethod
    def get_property(cls, key: str) -> str:
        """
        Extracts execution keys natively, mimicking Java's getProperty(key).
        """
        cls._load_properties()
        return cls._properties.get(key)
