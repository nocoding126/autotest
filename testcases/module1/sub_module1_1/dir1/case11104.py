from testbase import TestCase


class Demo11104(TestCase):  # 用例名（一个类一个用例）
    """基于qtaf的用例示例04"""  # 用例标题
    desc = ''  # 用例描述（可能没有该属性）
    owner = 'lucy'  # 归属人
    priority = TestCase.EnumPriority.High  # 优先级
    status = TestCase.EnumStatus.Ready  # 用例状态
    tags = "demo",  # 用例标签（可能没有该属性， 可能是str, tuple或set类型）
    timeout = 1  # 超时时间

    def pre_test(self):  # setup步骤（可能没有）
        """                                      # 预置条件描述（可能没有）
        1. 预置条件1
        1. 预置条件2
        """
        # ..具体步骤实现

    def run_test(self):  # 固定用例运行方法
        """                                      # 测试步骤及期望结果描述（可能没有）
        测试步骤：
        1. 测试步骤1
        2. 测试步骤2
        3. 测试步骤3

        期望结果
        2. 期望结果2
        3. 期望结果3

        """

        self.start_step('测试步骤1')  # 每个步骤的开始（可能没有）
        # ...步骤具体实现

        self.start_step('测试步骤2')
        # ...步骤具体实现

        self.start_step('测试步骤3')
        # ...步骤具体实现


if __name__ == '__main__':
    Demo11104().debug_run()