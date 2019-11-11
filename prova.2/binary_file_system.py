from base_classes.tree import BinaryTree, Node
import math
import os
import time
import platform


class FileNode(Node):
    def __init__(self, value, filename, right=None, left=None):
        super().__init__(value, right=right, left=left)
        self._filename = filename

    def __str__(self):
        return self._filename + '=' + str(self._data)

    def __iter__(self):
        if self.left:
            yield from self.left.traversal_inorder()
        yield self
        if self.right:
            yield from self.right.traversal_inorder()
        return

    @staticmethod
    def truncate(number, digits) -> float:
        stepper = 10.0 ** digits
        return int(math.trunc(stepper * number) / stepper)

    @staticmethod
    def file_time(path_to_file):
        """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        """
        if platform.system() == 'Windows':
            return os.path.getatime(path_to_file)
        else:
            stat = os.stat(path_to_file)
            try:
                return stat.st_atime_ns
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here, so we'll settle for when its content was last modified.
                return stat.st_mtime


class TreeDirectory(BinaryTree):

    def __init__(self, rootPath):
        super(TreeDirectory, self).__init__()
        key = FileNode.truncate(FileNode.file_time(rootPath), 3)
        rn = FileNode(key, rootPath)
        self.insert_node(rn)

    def insert_file(self, dirname, file):
        key = FileNode.truncate(FileNode.file_time(os.path.join(dirname, file)), 3)
        nf = FileNode(key, file)
        self.insert_node(nf)
        return

    def load_from_path(self, path=None, recursive=False):
        if path == None:
            path = os.getcwd()
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            if ((not recursive) and (r != path)):  # Aborta a carga para subdiretorios
                return
            for file in f:
                #self.insert_value(os.path.join(r, file))
                self.insert_file(r, file)
        return

    def purge(self, limitTime):
        for item in self.root_node:
            if item._data < limitTime:
                print( f'Removendo: { item } de { time.ctime( item._data )}')
                self.remove(item._data)
            else:
                print( f'Mantendo arquivo: { item } de { time.ctime( item._data )}')
        return
