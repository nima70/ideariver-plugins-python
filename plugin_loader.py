import importlib.util
import json
from validate_inputs import validate_inputs

class PluginLoader:
    def __init__(self, plugins_folder):
        self.plugins_folder = plugins_folder
        self.plugins = {}

    def load_metadata(self, metadata_file):
        """
        Load plugin metadata from a JSON file.
        """
        with open(metadata_file, 'r') as f:
            return json.load(f)

    def add_plugin(self, metadata_file):
        """
        Add a plugin to the system by loading its metadata and executable.
        """
        metadata = self.load_metadata(metadata_file)
        name_tag = metadata['nameTag']

        # Load the plugin's executable file dynamically
        spec = importlib.util.spec_from_file_location(name_tag, metadata['executableFile'])
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)

        # Manually reference the class name directly, assuming it is SumPlugin
        plugin_class = getattr(plugin_module, "SumPlugin")

        # Instantiate the plugin class
        plugin_instance = plugin_class()

        # Store plugin metadata and instance
        self.plugins[name_tag] = {
            'metadata': metadata,
            'instance': plugin_instance
        }

    def remove_plugin(self, name_tag):
        """
        Remove a plugin by its nameTag.
        """
        if name_tag in self.plugins:
            del self.plugins[name_tag]
        else:
            raise ValueError(f"No plugin found with nameTag '{name_tag}'")

    def init_plugin(self, name_tag, services):
        """
        Initialize the plugin by passing utility services.
        """
        if name_tag not in self.plugins:
            raise ValueError(f"No plugin found with nameTag '{name_tag}'")

        # Initialize the plugin with services
        plugin_instance = self.plugins[name_tag]['instance']
        plugin_instance.init(services)

    def run_plugin(self, name_tag, input_data):
        """
        Execute the run method of a plugin, with input validation.
        """
        if name_tag not in self.plugins:
            raise ValueError(f"No plugin found with nameTag '{name_tag}'")

        # Get plugin metadata and validate inputs
        plugin_metadata = self.plugins[name_tag]['metadata']
        validate_inputs(plugin_metadata, input_data)

        # Execute the run method of the plugin
        plugin_instance = self.plugins[name_tag]['instance']
        return plugin_instance.run(input_data)

    def list_plugins(self):
        """
        List all loaded plugins and their metadata.
        """
        return {tag: plugin['metadata'] for tag, plugin in self.plugins.items()}
