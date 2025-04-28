class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    # ----------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Creates instance variables (status, muted, volume, and channel)
        for the class Television.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
# ----------------------------------------------------------------------------------------------------------------
    def power(self) -> None:
        """
        Turns the TV on or off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    # ----------------------------------------------------------------------------------------------------------------
    def mute(self) -> None:
        """
        Mutes the TV if the TV is on by setting the muted variable and changing the volume minimum.
        """
        if self.__status and not self.__muted:
            self.__muted = True
            self.__volume = self.MIN_VOLUME
        elif self.__status and self.__muted:
            self.__muted = False

    # ----------------------------------------------------------------------------------------------------------------
    def channel_up(self) -> None:
        """
        Increases the TV channel.
        Increases the channel if it is not on the maximum.
        If it is, it changes to the minimum.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1

    # ----------------------------------------------------------------------------------------------------------------
    def channel_down(self) -> None:
        """
        Decreases the TV channel of the TV.
        Decreases the channel if it is not on the minimum channel.
        If it is, it changes to the maximum.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1

    # ----------------------------------------------------------------------------------------------------------------
    def volume_up(self) -> None:
        """
        Increases the volume of the TV.
        Increases the volume if it is not the max volume.
        If it is the max then it does nothing.
        As well changes the muted and volume variable if it was already muted.
        Unmutes and sets to max volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.MAX_VOLUME
            if self.__volume != self.MAX_VOLUME:
                self.__volume = self.__volume + 1

    # ----------------------------------------------------------------------------------------------------------------
    def volume_down(self) -> None:
        """
        Decreases the volume of the TV.
        Decreases the volume if it is not the min volume.
        If it is the min then it does nothing.
        As well changes the muted and volume variable if it was already muted.
        Unmutes and set to max volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.MAX_VOLUME
            if self.__volume != self.MIN_VOLUME:
                self.__volume = self.__volume - 1

    # ----------------------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        """
        Returns string with variables (Power, Channel, and Volume)
        "Power = [status], Channel = [channel], Volume = [volume]"
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"