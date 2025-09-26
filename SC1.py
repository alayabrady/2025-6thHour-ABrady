#Name:Alaya
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
enemy_dict={
    "enemy 1":{
        "name":"sid",
        "health":1000,
        "damage":100
    },
    "enemy 2":{
        "name":"buzz lightyear",
        "health":80,
        "damage":30,
    },
    "enemy 3":{
        "name":"woody",
        "health":40,
        "damage":50,
    },
    "enemy 4":{
        "name":"aliens",
        "health":20,
        "damage":10,
    },
    "enemy 5":{
        "name":"rex",
        "health":100,
        "damage":30,
    },

}
enemy_dict["enemy 1"].update({"damage" :int(input("whats the damage of enemy 1")) })
print(enemy_dict["enemy 1"])

enemy_dict["enemy 2"].update({"damage" :int(input("whats the damage of enemy 2")) })
print(enemy_dict["enemy 2"])

enemy_dict["enemy 3"].update({"damage" :int(input("whats the damage enemy 3")) })
print(enemy_dict["enemy 3"])

enemy_dict["enemy 4"].update({"damage" :int(input("whats the damage enemy 4")) })
print(enemy_dict["enemy 4"])

enemy_dict["enemy 5"].update({"damage" :int(input("whats the damage enemy 5")) })
print(enemy_dict["enemy 5"])

