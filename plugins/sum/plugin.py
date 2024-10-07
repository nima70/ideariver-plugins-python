from plugin_base import BasePlugin

class SumPlugin(BasePlugin):
    """
    Plugin that calculates the sum of 'a' and 'b' from a given JSON input.
    """

    def __init__(self):
        self.services = None

    def init(self, services):
        """
        Initialize the plugin with required services. (Not used in this example)
        
        Args:
            services (dict): Dictionary of services (e.g., logging).
        """
        self.services = services

    def run(self, input_data):
        """
        Calculate the sum of 'a' and 'b' from the input JSON.

        Args:
            input_data (dict): Dictionary with 'a' and 'b'.

        Returns:
            dict: Dictionary with the sum of 'a' and 'b'.
        """
        a = input_data.get('a')
        b = input_data.get('b')
        return {"sum": a + b}
