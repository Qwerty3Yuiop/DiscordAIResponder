import gemini_access
import discord_access
import os

def respond_last():
    history = channel.searchHistory()
    content = history[0]["content"]
    message = session.send(content)
    print(message)
    if input("Approve [y/n]: ").lower() == "y":
        response = channel.sendMsg(message)
        print(f"Completed : {response}")


if __name__ == "__main__":
    # setting env variables and other fields
    os.environ["GOOGLE_API_KEY"] = ""
    os.environ["DISCORD_AUTH_KEY"] = ""
    channelID = 0
    

    session = gemini_access.AISession()
    channel = discord_access.DiscordChannel(channelID)

    if(os.environ["GOOGLE_API_KEY"] == "" or os.environ["DISCORD_AUTH_KEY"] == ""):
        print("you must set environment variable in main.py")
        exit()

    while(True):
        match input(""):
            case "respond":
                respond_last()
            case "testsend":
                print(channel.sendMsg("testsend"))
            case _:
                break
        

