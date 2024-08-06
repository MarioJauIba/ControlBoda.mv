document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {onCloseEnd: function() {
        console.log('Modal closed!');
    }});
    var tabs = document.querySelector('.tabs');  
    var tabInstances = M.Tabs.init(tabs, {});
});

async function writeClipboardText(text) {
    try {
      await navigator.clipboard.writeText(text);
    } catch (error) {
      console.error(error.message);
    }
}