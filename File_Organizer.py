import os
import sys
import shutil

def file_organizer():
    try:
        path = input("File Organizer started. Organizing files in directory(Absolute Path):")
       
        if not os.path.isabs(path) or os.path.isfile(path):
            raise ValueError("Error: Please enter an absolute path to a valid directory.") 
        
        
        # Define file type extensions
        extns_m = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
        extns_v = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
        extns_d = ['.pdf', '.docx', '.xlsx', '.pptx', '.txt']
        extns_i = ['.jpg', '.png', '.gif', '.bmp', '.svg']
        extns_o = ['.exe', '.dll', '.bat', '.py', '.html', '.css', '.zip', '.tar.gz', '.rar', '.7z', '.iso']

        # Flags to track which types of files are present
        mflag = False
        vflag = False
        dflag = False
        iflag = False
        oflag = False
        
        # Checking which extensions are present
        for file in os.listdir(path):
            name,extns = os.path.splitext(file)
            if extns in extns_m:
                mflag = True
            elif extns in extns_v:
                vflag = True
            elif extns in extns_d:
                dflag = True
            elif extns in extns_i:
                iflag = True
            elif extns in extns_o:
                oflag = True

        # creating the directories for the present extensions
        print("Creating directories for file types:")
        dir = 0

        if iflag and not os.path.exists(os.path.join(path, "Images")):
            dir += 1
            image = os.path.join(path, "Images")
            os.makedirs(image)
            print(f"- Created Directory: {image}")

        if dflag and not os.path.exists(os.path.join(path, "Documents")):
            dir += 1
            doc = os.path.join(path, "Documents")
            os.makedirs(doc)
            print(f"- Created Directory: {doc}")

        if vflag and not os.path.exists(os.path.join(path, "Videos")):
            dir += 1
            vid = os.path.join(path, "Videos")
            os.makedirs(vid)
            print(f"- Created Directory: {vid}")

        if mflag and not os.path.exists(os.path.join(path, "Music")):
            dir += 1
            mus = os.path.join(path, "Music")
            os.makedirs(mus)
            print(f"- Created Directory: {mus}")

        if oflag and not os.path.exists(os.path.join(path, "Other")):
            dir += 1
            other = os.path.join(path, "Other")
            os.makedirs(other)
            print(f"- Created Directory: {other}")
        
        # Moving the files from the original to destined directory
        print("Moving files...")
        num_of_files = 0
        files_moved = 0
        for file in os.listdir(path):
            num_of_files += 1
            name,extns = os.path.splitext(file)
            
            if extns in extns_m:
                shutil.move(os.path.join(path,file),mus)
                print(f"- Moving file: {file} to {mus}")
                files_moved += 1
            elif extns in extns_v:
                shutil.move(os.path.join(path,file),vid)
                print(f"- Moving file: {file} to {vid}")
                files_moved += 1
            elif extns in extns_d:
                shutil.move(os.path.join(path,file),doc)
                print(f"- Moving file: {file} to {doc}")
                files_moved += 1
            elif extns in extns_i:
                shutil.move(os.path.join(path,file),image)
                print(f"- Moving file: {file} to {image}")
                files_moved += 1
            elif extns in extns_o:
                shutil.move(os.path.join(path,file),other)
                print(f"- Moving file: {file} to {other}")
                files_moved += 1
        
        #Summary of Organization
        print("File organization completed successfully.")
        print("Summary:")
        print(f"- {num_of_files} files processed.")
        print(f"- {files_moved} Files categorized into {dir} directories.")
        sys.exit()
    
    except Exception as e:
        print(f"Error found: {e}")
    
if __name__ == "__main__":
    file_organizer()