# First we have to install plyer library--> pip install plyer
from plyer import notification
notification.notify(title="Message from your system", message="GOOD MORNING",
                    timeout=20)
