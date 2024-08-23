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
    if (style===undefined){
        document.head.appendChild(document.createElement('style'))
        style.type = 'text/css';
    }
    style.innerHTML += '.bd {border:2px dashed red!important;}';
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
