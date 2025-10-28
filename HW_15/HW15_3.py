#Task 3

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController :
    # save the list of channels and set the current index to 0, it is channel 1 for the user
    def __init__(self, channels):
        self.channels = channels
        # set the first channel
        self.current = 0

    # move the index to the beginning as first channel
    def first_channel(self) :
        # set the first channel
        self.current = 0
        return self.channels[self.current]

    # move the index to the end as the last channel
    def last_channel(self) :
        #  the last one
        self.current = len(self.channels) - 1
        return self.channels[self.current]

    def turn_channel(self, n) :
        # converts user number N  to an index as Python number(inner_number) n-1
        inner_number = n - 1
        # check that the channel exists
        if 0 <= inner_number < len(self.channels) :
            self.current = inner_number
            return self.channels [self.current]
        return self.channels [self.current]

    def next_channel (self) :
        # next channel
        self.current +=1
        # if end of list, go to start
        if  self.current >= len (self.channels) :
            self.current = 0
            return self.channels [self.current]
        return self.channels [self.current]

    def previous_channel(self) :
        # previous channel
        self.current -=1
        # if it was the first one go to the last one
        if self.current < 0 :
            self.current = len(self.channels) - 1
            return self.channels[self.current]
        return self.channels[self.current]

    def current_channel(self):
        # return the current channel
        return self.channels[self.current]

    def exists (self, name) :
        # if it's a number : check the range
        if isinstance(name, int) :
            return "YES" if 1<=name <= len(self.channels) else "NO"
        # if text — check if it's in the list
        if isinstance(name, str) :
            return "YES" if name in self.channels else "NO"
        return "NO"

controller = TVController(CHANNELS)

print(controller.first_channel())  # BBC
print(controller.last_channel())  # TV1000
print(controller.turn_channel(1))  # BBC
print(controller.next_channel())  # Discovery
print(controller.previous_channel())  # BBC
print(controller.current_channel())  # BBC
print(controller.exists(4))  # No
print(controller.exists("BBC"))








