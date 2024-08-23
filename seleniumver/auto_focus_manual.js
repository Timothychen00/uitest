escapeHTMLPolicy = trustedTypes.createPolicy("forceInner", {
    createHTML: (to_escape) => to_escape
});
window.hovered_element = null;
window.last = null;
_get_index = (d_child,d_parent) => Array.prototype.indexOf.call(d_parent.children,d_child)
function find(e) {
	var _s = e.tagName;
	if(e.id) _s += '#' + e.id;
	if(e.classList) _s +=  Array.prototype.map.call(e.classList,d=>'.'+d).join('')
	let parent = e.parentElement;
	if(parent) _s = find(parent) + ' > ' + _s +`:nth-child(${_get_index(e,parent)+1})` ;
	return _s;
}
function track_mouse(event) {
    var x = event.clientX, y = event.clientY;
    var element = document.elementFromPoint(x, y);
    if (!element) {

        window.hovered_element = null;
        return;
    }
    var style = document.getElementsByTagName('style')[0];
    if (style === undefined) {
        document.head.appendChild(document.createElement('style'))
        style.type = 'text/css';
    }
    style.innerHTML += '.bd {border:2px dashed red!important;}';
    window.last = window.hovered_element;
    window.hovered_element = element;
    element.classList.add('bd');

    if (window.last != window.hovered_element && window.last && window.hovered_element) {
        window.last.classList.remove('bd');
    }

}

window.onmousemove = track_mouse;
window.onkeypress = (e) => {
    if (e.code == "KeyS") {
        window.pres = 1;
        window.element_xpath = find(window.hovered_element);
        console.log(window.element_xpath)
    }
}
