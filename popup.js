document.getElementById("summarizeBtn").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        function: extractAndSummarize
      });
    });
  });
  
  function extractAndSummarize() {
    chrome.runtime.sendMessage({ action: "extractText" }, async (response) => {
      if (response && response.content) {
        let summary = await fetchSummary(response.content);
        document.getElementById("summary").innerText = summary;
      }
    });
  }
  
  async function fetchSummary(text) {
    let res = await fetch("https://your-api-url.com/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });
    let data = await res.json();
    return data.summary;
  }
   
