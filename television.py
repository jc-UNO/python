# Made in collaboration with Jake Amundsen

class Television:
    # Class constants
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the television with default settings."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Turn the TV on or off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the TV when it is on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase channel by 1. Wrap around to MIN_CHANNEL if at MAX_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decrease channel by 1. Wrap around to MAX_CHANNEL if at MIN_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increase volume by 1 if not at max. Unmute if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease volume by 1 if not at min. Unmute if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return a string representation of the TV's state."""
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


# echo "# python" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jc-UNO/python.git
# git push -u origin main
# token
