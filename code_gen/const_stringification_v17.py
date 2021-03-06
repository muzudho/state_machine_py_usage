from code_gen.const_conf_v17 import ConstConf


class ConstStringification:
    @classmethod
    def stringify(clazz, const_conf_py_dict):
        const_conf = ConstConf(const_conf_py_dict)

        text = ""

        for key, value in const_conf.data.items():
            text += f"{key} = '{value}'\n"

        return text
