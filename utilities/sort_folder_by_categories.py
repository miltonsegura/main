#!/usr/bin/python3
import os
import shutil
import sys

def main(loc=None, excluded=[], silent=False):
    """Sorts files into categories.
    
    Sorts each file (excluding itself), according to its extension, into folders
    created for each category. New files are moved, existing files are
    overwritten.

    A summary is printed can be printed after all files are moved.

    Args:
        loc: A path to an existing folder to sort. (default os.getcwd())
        excluded: A list of filenames to be ignored. (default [this_filename])
        silent: Wether it should print the summary at the end

    Returns:
        A dict mapping each category to the files that were moved

    Raises:
        OSError: It wasn't possible to create a folder
        PermissionError: A file couldn't be moved or overwritten.
    """

    # Set default parameters
    if loc is None:
        loc = os.getcwd()
    assert os.path.exists(loc)

    this_filename = os.path.split(sys.argv[0])[-1]
    if excluded is None:
        excluded = [this_filename]
    else:
        excluded = [this_filename] + excluded
    assert type(excluded) is list

    # Initialize variables 
    categories = {'gDesktop Plugins' : {'gg', 'ggc'},
                  'Torrents'         : {'torrent'},
                  'Docs'             : {'doc', 'xls', 'ppt', 'mdb', 'pub',
                                        'docx', 'pptx', 'xlsx', 'pdf', 'rtf',
                                        'ppsx', 'csv', 'vcf', 'txt', 'text'},
                  'Images'           : {'jpg', 'jpeg', 'png', 'gif', 'psd',
                                        'psb', 'ai', 'svg', 'dng'},
                  'Videos'           : {'mpg', 'mp4', 'mkv', 'srt', 'wmv'
                                        'mov'},
                  'Audio'            : {'mp3', 'wma'},
                  'Programming'      : {'py', 'pyc', 'pyo', 'pyw', 'pl', 'v',
                                        'c', 'dat', 'ecf', 'unitypackage'},
                  'Executables'      : {'exe', 'msi', 'apk', 'bat', 'jar',
                                        'jnlp', 'swf', 'reg', 'vbox-extpack'},
                  'Compressed'       : {'rar', 'zip', 'iso', 'tgz', 'gz', '7z',
                                        'ova'}}

    summary = dict((category, []) for category in categories)
    filenames = (filename for filename in os.listdir(loc)
                 if os.path.isfile(filename)
                 and filename not in excluded)

    # Begin sorting
    for filename in filenames:
        for category, extensions in categories.items():
            for extension in extensions:
                if filename.lower().endswith('.' + extension):
                    src = loc
                    src_path = os.path.join(src, filename)
                    dst = os.path.join(loc, category)
                    dst_path = os.path.join(dst, filename)
                    # Create category folder
                    if not os.path.exists(dst):
                        try:
                            os.mkdir(dst)
                        except OSError:
                            print ('Failed to create folder:',
                                   categories[category])
                    # Move/copy the files
                    try:
                        if not os.path.exists(dst_path):
                            shutil.move(src_path, dst)
                        else:
                            shutil.copy2(src_path, dst)
                            os.remove(src_path)
                        summary[category].append(filename)
                    except PermissionError:
                        print('PermissionError '
                              '({}):'.format(os.stat(src).st_mode),
                              src)
                    break

    # Print a summary at the end
    if not silent:
        for category, filenames in summary.items():
            if filenames:
                print ('{} files moved to {}'.format(len(filenames), category))
                for filename in filenames:
                    print (' '*2 + filename)
        os.system('pause')
        
    return summary


if __name__ == '__main__':
    silent = '--silent' in sys.argv
    if silent:
        sys.argv.remove('--silent')
    if len(sys.argv) == 1:
        main(silent=silent)
    elif len(sys.argv) == 2:
        main(loc=sys.argv[1],
             silent=silent)
    else:
        main(loc=sys.argv[1],
             exclude=sys.argv[2:],
             silent=silent)
