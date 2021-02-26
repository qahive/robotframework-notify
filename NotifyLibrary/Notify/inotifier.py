from abc import ABC, abstractmethod


class iNotifier(ABC):

    @abstractmethod
    def send_notify(self):
        pass
    
