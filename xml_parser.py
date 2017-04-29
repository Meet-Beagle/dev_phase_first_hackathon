import xml.etree.ElementTree as Et
import json
import _utils


def basic_read():
    tree = Et.parse('mock_data.xml', )
    root = tree.getroot()
    print(root.tag)
    # print(dict(root))
    for child in root:
        print(child.tag, child.attrib)
        print('    |')
        for grand_child in child:
            print('    |', 8*'-', grand_child.tag, grand_child.text)


class RawData:
    def __init__(self, conference, date, location):
        self.conference = conference
        self.date = date
        self.location = location

    @classmethod
    def parse(cls, data, *tags):
        return cls(*tuple(hierarchical_dict_parser(data, tag) for tag in tags))

    def dump(self, name, path=None, data_format=('.json',)):
        _utils._if_not_exist_mkdir(path)
        filename = _utils._make_filename(path, name)
        data = dict(conference=self.conference,
                    date=self.date,
                    location=self.location)

        if '.json' in data_format:
            json_name = '.'.join((filename, 'json'))
            print(json_name)
            with open(json_name, 'w') as json_file:
                json.dump(data, json_file)

        if '.dat' in data_format:
            dat_name = '.'.join((filename, 'dat'))
            print(dat_name)
            with open(dat_name, 'w') as dat_file:
                for key, value in data.items():
                    dat_file.write(f'{key}: {value} \n')

    @staticmethod
    def load(name, path=''):
        _utils._if_not_exist_mkdir(path)
        _utils._make_filename(path, name)
        with open('mock_data.json') as file:
            j_text = file.read()
            # print(j_text)
            data = json.loads(j_text)
            # print('data', data)
            return data


def hierarchical_dict_parser(hierarchical_dict: dict, tag: str):
    val = hierarchical_dict
    for key in tag.split('/'):
        val = val.get(key)
    return val


class RawDataTest:
    @staticmethod
    def basic_test():
        data_dict = RawData.load(name='mock_data.json')
        print(data_dict)
        RawData.parse(data_dict,
                      'widget/debug',
                      'widget/image',
                      'widget/text').dump('saved',
                                          data_format=['.json', '.dat'])


def hierarchical_dict_parser_test():
    dd = {'0': {'1': {'last': 'val'}}}
    tag = '0'

    print('dd before:', dd)
    print(hierarchical_dict_parser(dd, tag))
    print('dd after:', dd)
    print(dd[tag])


if __name__ == '__main__':
    RawDataTest.basic_test()
