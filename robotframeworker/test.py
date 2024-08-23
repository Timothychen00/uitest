import inquirer
from robot.running import TestSuiteBuilder
from robot.model import SuiteVisitor
from inquirer.themes import Default

filename='SAA006.robot'

class TestCasesFinder(SuiteVisitor):
    def __init__(self):
        self.tests = []

    def visit_test(self, test):
        self.tests.append(test)
        
builder = TestSuiteBuilder()
testsuite = builder.build('tests/'+filename)
finder = TestCasesFinder()
testsuite.visit(finder)

scanned_tasks=[task.name for task in finder.tests]
print('scanned:',scanned_tasks)


class WorkplaceFriendlyTheme(Default):
    """Custom theme for checkbox profix"""

    def __init__(self):
        super().__init__()
        self.Checkbox.selected_icon = "[O]"
        self.Checkbox.unselected_icon = "[ ]"



def get_selection_order(options):
    selected_order = []
    question = [
        inquirer.Checkbox(
            'choices',
            message="請選擇選項（可跳過）",
            choices=options
        )
    ]

    answer = inquirer.prompt(question,theme=WorkplaceFriendlyTheme())['choices']
    selected_order.extend(answer)
    # 從選項中移除已選擇的項目
    options = [opt for opt in options if opt not in answer]
    return selected_order


# 初始化選項列表
options = scanned_tasks=[task.name for task in finder.tests]
# 獲取選擇順序
selection_order = get_selection_order(options)

print("使用者選擇的順序：", selection_order)