import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://shauryauniyal:bNOz0z1VIeGN3Co1@youtubemanager.dyveoir.mongodb.net/", tlsAllowInvalidCertificates = True)

db = client["ytmanager"]

video_collection = db["videos"]

def list_all_videos():
    print("\n")
    print("*" * 70)
    for video in video_collection.find():
        print(f"Video ID: {video['_id']}, Name: {video['Name']}, Time: {video['Time']}")
    print("\n")
    print("*" * 70)

def add_video(name, time):
    video_collection.insert_one({'Name': name, 'Time': time})

def update_video(id, new_name, new_time):
    video_collection.update_one({"_id": ObjectId(id)}, {"$set": {"Name": new_name, "Time": new_time}})

def delete_video(id):
    video_collection.delete_one({"_id": ObjectId(id)})

def main():
    while True:
        print("\nYoutube Manager | Choose your option")
        print()
        print("*" * 70)
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the application")

        choice = int(input("Enter your choice (1 to 9): "))

        match choice:
            case 1:
                list_all_videos()
            case 2:
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case 3:
                list_all_videos()
                id = input("Enter the id of the video you want to update: ")
                new_name = input("Enter the new name: ")
                new_time = input("Enter the new time: ")
                update_video(id, new_name, new_time)
            case 4:
                list_all_videos()
                id = input("Enter the id of the video you want to delete: ")
                delete_video(id)
            case 5:
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()