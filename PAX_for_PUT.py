import shutil, os, configparser

# Set up config
config = configparser.ConfigParser()
config.read('pax_config.cfg')

# Define the folders for PAX representations
PRESERVATION_DIR = 'Representation_Preservation'
ACCESS_DIR = 'Representation_Access'

# Get access and preservation formats from config file 
PRESERVATION_FMT = config.get('formats', 'preservation_format')
ACCESS_FMT = config.get('formats', 'access_format')

# Get root directory from config file
def get_top_dir() -> str:
    top_dir = config.get('directory', 'top_dir')
    if config.getboolean('directory', 'use_hard_link'):
        hard_link_dir = os.path.join(top_dir, os.path.basename(top_dir)+'_HARDLINK')
        shutil.copytree(top_dir, hard_link_dir, copy_function=os.link)
        top_dir = hard_link_dir   
    return top_dir 
    
# Iterate over entire collection
for root, dirs, files in os.walk(get_top_dir()):

    # Get required names for new sub-folders by stripping file extensions
    new_subfolders = [file.split('.')[0] for file in files]

    # Iterate over new list of required folders (converting to a set removes duplicates)
    for sub_folder in set(new_subfolders):
        print(sub_folder)

        # Create new PAX-folder with representation folders 
        pax_folder_path = os.path.join(root, sub_folder + '.pax')
        os.mkdir(pax_folder_path)
        os.mkdir(os.path.join(pax_folder_path, PRESERVATION_DIR))
        os.mkdir(os.path.join(pax_folder_path, ACCESS_DIR))

        # Push files in to PAX folders
        for file in files:
            file_path = os.path.join(root, file)
            
            if sub_folder in file:
                if file.endswith(PRESERVATION_FMT):
                    shutil.move(file_path, os.path.join(pax_folder_path, PRESERVATION_DIR))
                if file.endswith(ACCESS_FMT):
                    shutil.move(file_path, os.path.join(pax_folder_path, ACCESS_DIR))
