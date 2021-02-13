"""
Dataset for storing a user's reminder, server, and userID.
Tyler Pease, 2021
"""


class remindUser:
    # This needs to be tackled later to handle specific times.
    # At the moment I think I can only really tackle dates.

    def __init__(self, guildID, userID, date, reminder):
        self.guildID = guildID
        self.userID = userID
        self.date = date

    def getGuild(self):
        return self.guildID

    def getUser(self):
        return self.userID

    def getDate(self):
        return self.date


    #def getTime(self):
    #    return self.time


    def getReminder(self):
    #    This should be the reminder message that the user dictates.
        return self.reminder
