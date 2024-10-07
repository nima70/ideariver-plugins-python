from abc import ABC, abstractmethod

class BasePlugin(ABC):
    """
    Abstract base class for all plugins. 
    Developers must implement the `init` and `run` methods.
    """

    @abstractmethod
    def init(self, services):
        """
        Initialize the plugin with the required services.
        
        Args:
            services (dict): Dictionary of services (e.g., logging, text summarization).
        """
        pass

    @abstractmethod
    def run(self, input_data):
        """
        Execute the plugin's logic.
        
        Args:
            input_data (dict): Data to be processed by the plugin.
            
        Returns:
            str: Result after processing.
        """
        pass