import time

from icecream import ic
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from __init__ import initialize

driver=initialize()

driver.get('https://stackoverflow.com/questions/61964265/getting-error-this-document-requires-trustedhtml-assignment-in-chrome')

js = '''
escapeHTMLPolicy = trustedTypes.createPolicy("forceInner", {
    createHTML: (to_escape) => to_escape
});
window.hovered_element = null;
window.last = null;
function createXPathFromElement(elm) { 
    var allNodes = document.getElementsByTagName('*'); 
    for (var segs = []; elm && elm.nodeType == 1; elm = elm.parentNode) 
    { 
        if (elm.hasAttribute('id')) { 
                var uniqueIdCount = 0; 
                for (var n=0;n < allNodes.length;n++) { 
                    if (allNodes[n].hasAttribute('id') && allNodes[n].id == elm.id) uniqueIdCount++; 
                    if (uniqueIdCount > 1) break; 
                }; 
                if ( uniqueIdCount == 1) { 
                    segs.unshift('id("' + elm.getAttribute('id') + '")'); 
                    return segs.join('/'); 
                } else { 
                    segs.unshift(elm.localName.toLowerCase() + '[@id="' + elm.getAttribute('id') + '"]'); 
                } 
        } else if (elm.hasAttribute('class')) { 
            segs.unshift(elm.localName.toLowerCase() + '[@class="' + elm.getAttribute('class') + '"]'); 
        } else { 
            for (i = 1, sib = elm.previousSibling; sib; sib = sib.previousSibling) { 
                if (sib.localName == elm.localName)  i++; }; 
                segs.unshift(elm.localName.toLowerCase() + '[' + i + ']'); 
        }; 
    }; 
    return segs.length ? '/' + segs.join('/') : null; 
}; 
function track_mouse(event) {
    var x = event.clientX, y = event.clientY;
    var element = document.elementFromPoint(x, y);
    if (!element) {

        window.hovered_element = null;
        return;
    }
    var style = document.getElementsByTagName('style')[0];
    try
    style.innerHTML += '.bd {border:2px dashed red!important;}';
    catch
    style
    window.last = window.hovered_element;
    window.hovered_element = element;
    element.classList.add('bd');
    window.element_xpath=createXPathFromElement(window.hovered_element);
    console.log(window.element_xpath)
    if (window.last != window.hovered_element && window.last && window.hovered_element) {
        window.last.classList.remove('bd');
    }

}

window.onmousemove = track_mouse;
window.onkeypress=(e)=>{
    if(e.code=="KeyS")
        window.pres=1;
}

'''

driver.execute_script(js)
while True:
    element = driver.execute_script('return window.hovered_element;')
    a = driver.execute_script('return window.pres;')
    path = driver.execute_script('return window.element_xpath')
    if element:
        print(f'当前鼠标所在的标签为：{element.tag_name}, 其中的文本内容为：{element.get_attribute("innerHTML")}')
        if a==1:
            ic(element.tag_name,path)
            element.screenshot(f'screenshots/{element.tag_name}.png')
            element.find_element(By.XPATH,"..").screenshot(f'screenshots/{element.tag_name}-father.png')
            driver.execute_script('window.pres=0;')
            break
    time.sleep(0.1)
driver.quit()

ic('new round')
driver=initialize()
driver.get('https://stackoverflow.com/questions/61964265/getting-error-this-document-requires-trustedhtml-assignment-in-chrome')
action = ActionChains(driver) 
element=driver.find_element(By.CSS_SELECTOR,"#question-header > div > div > a")
action.move_to_element(element).perform() 
time.sleep(3)
element.screenshot(f'screenshots/target.png')
parent=element.find_element(By.XPATH,'..').screenshot(f'screenshots/target-parent.png')


