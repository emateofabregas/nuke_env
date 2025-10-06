def createReads():
    def find_versions(directory):  
        # List all folders in the directory that match the pattern 'v' followed by three digits
        try:
            versions = [name for name in os.listdir(directory) if re.match(r'v\d{3}', name)]
        
            # Sort the versions in descending order by their numerical value
            versions.sort(reverse=True, key=lambda v: int(v[1:]))  # Sort by numerical value, highest first
            
            print(f"Versions found in {versions}")
            return versions
            
        except FileNotFoundError:
            print("File not found, skipping...")
            
            
    def find_files(directory, file_exts):
        found_files = []
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in file_exts):
                    found_files.append(os.path.join(root, file))
        
        return found_files
        
        
    def search_versions(directory, version_type):
        for version in version_type:
            versioned_path = os.path.join(directory, version)
            found_files = find_files(versioned_path, '.exr')
                
            if found_files:
                latest_file = max(found_files, key=os.path.getmtime)
                base, ext = os.path.splitext(latest_file)
                sequence_path = re.sub(r'(\d+)$', '%04d', base) + ext
                frame_range = re.search(r'(\d+)$', base).group(1) if re.search(r'(\d+)$', base) else None
                print(frame_range)

            return found_files, frame_range
    
    
    def createRenders():                    
        root_name = nuke.Root().name()
        root_split = root_name.split('/')
        project = root_split[5]
        
        directory = 'E:/renders/' + project + '/'
        if directory:
            versions = find_versions(directory)
            found_files, frame_range = search_versions(directory, versions)    
            print(frame_range)
            
            for fo in found_files:
                if fo.endswith(frame_range+'.exr'):
                    path = fo.replace(frame_range, '%04d')
                    read = nuke.createNode('Read')
                    read['file'].setValue(path)
                    read['on_error'].setValue('nearest_frame')
                    read['first'].setValue(int(frame_range))
                    read['last'].setValue(int(frame_range))