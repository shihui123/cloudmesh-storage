import os
from pprint import pprint

import cloudmesh.storage.provider.box.Provider
from cloudmesh.common.util import HEADING
from cloudmesh.common.util import path_expand


# nosetest -v --nopature
# nosetests -v --nocapture tests/test_box.py

class TestBox:

    def setup(self):
        self.p = cloudmesh.storage.provider.box.Provider.Provider(service="box")

        self.source = "set the source location here and use in tests"
        self.destination = "set the destination location here and use in tests"


    def test_01_put(self):
        HEADING()

        # TODO: test must be done in ~/.cloudmesh not ~
        # use Path(filename) so this also works on windows

        src_path = path_expand('~/test_folder')
        if not os.path.exists(src_path):
            os.makedirs(src_path)
        f = open(src_path+'/test.txt', 'w')
        # TODO use named arguments
        test_file = self.p.put('~/test_folder/test.txt', '/')
        pprint(test_file)

        assert test_file is not None

    def test_02_get(self):
        HEADING()
        self.test_01_put()
        # TODO use named arguments
        file = self.p.get('/test.txt', '~/test_folder')
        pprint(file)

        assert file is not None

    def test_03_list(self):
        HEADING()
        # TODO use named arguments
        contents = self.p.list('/')
        for c in contents:
            pprint(c)

        assert len(contents) > 0

    def test_04_search(self):
        HEADING()
        # TODO use named arguments
        search_files = self.p.search('/', 'test.txt', True)
        pprint(search_files)

        assert len(search_files) > 0

    def test_05_create_dir(self):
        HEADING()
        # TODO use named arguments
        dir = self.p.create_dir('/testdir')
        pprint(dir)

        assert dir is not None

    def test_06_delete(self):
        HEADING()
        # TODO use named arguments
        self.p.delete('testdir')



















