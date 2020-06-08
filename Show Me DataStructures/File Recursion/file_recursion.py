import os

root = "testdir"


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if (os.path.isdir(path) or os.path.isfile(path)) is not True:
        return None

    data = os.listdir(path=path)

    resultant_urls = []

    for val in data:
        url = os.path.join(path, val)
        if os.path.isfile(url):
            if url.endswith(suffix):
                resultant_urls.append(url)
        else:
            resultant_urls += find_files(suffix, url)
    return resultant_urls


print(find_files(".c", root))  # print ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']
print(find_files(".h", root))  # print ['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h', 'testdir/subdir1/a.h']
print(find_files(".txt", root))  # print []
print(find_files(".txt", "asdasdas"))  # print None
print(find_files(".txt", ""))  # print None
print(find_files("asdas", root))  # print []
