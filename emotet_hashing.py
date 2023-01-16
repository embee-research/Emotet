"""
Emotet API hashing script
@embee_research @HuntressLabs
"""

import pefile,sys,os

"""
Hashes are xor'd with a key after calcuation
This value does change between samples
and may need to be updated

The value can typically be found after a call to the hash calculation
See the readme for an example of this

#[0x137ef56a,0x343e9b56] - Common Values, Try these first
"""
#UPDATE THIS VALUE
xor_value = 0x137ef56a 


#Calculate Emotet DJB2-style hash
def calc_hash(name):
    output = 0
    for c in name:
        output = output * 0x1003f + ord(c)
    output = output & 0xffffffff
    output = output ^ xor_value
    #uncomment the hex piece to return decimal values
    return hex(output)

#Parse the export list from a dll file
def get_export_list(path_to_file):
    pe = pefile.PE(path_to_file)
    d = [pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_EXPORT"]]
    pe.parse_data_directories(directories=d)
    exports = [(e.name) for e in pe.DIRECTORY_ENTRY_EXPORT.symbols]
    return exports

def get_cwd_dll():
    dll_list = []
    cwd = os.listdir()
    for filename in cwd:
        if ".dll" in filename:
            dll_list.append(filename)
    return dll_list

def build_export_list(dll_list):
    #For each DLL, get the exports, build a master list
    export_master_list = []
    for file_name in dll_list:
        try:
            export_master_list += get_export_list(file_name)
        except:
            print("Failed to open {}".format(file_name))
            continue
    return export_master_list

def build_hash_dictionary(export_master_list):
    #resolve each export name and calculate hashes
    hash_dict = {}
    for export_name in export_master_list:
        if export_name:
            try:
                export_name = export_name.decode()
            except:
                export_name = export_name.decode('utf-16')
                continue
            h = calc_hash(export_name)
            hash_dict[export_name] = h
            hash_dict[h] = export_name
    return hash_dict

def lookup_hash(hash_dict, value):
    try:
        return hash_dict[value]
    except Exception as e:
        print(e)
        print("Unable to Find value {}".format(lookup))
        sys.exit(1)



def main():
    #Check that at least 1 argument has been provided
    try:
        lookup = sys.argv[1]
    except:
        print("failed to parse args")
        sys.exit(1)
        
    #Enumerate DLL's from current directory
    dll_list = get_cwd_dll()
    export_master_list = build_export_list(dll_list)
    hash_dict = build_hash_dictionary(export_master_list)
  
    
    #perform the lookup
    try:
        print("{} : {}".format(lookup,lookup_hash(hash_dict,lookup)))
    except:
        print("Failed to Find value")
        sys.exit(1)
    
if __name__ == "__main__":
    main()






    



