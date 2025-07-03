import React from "react";
import FileUpload from "./components/FileUpload";
// import SummaryDisplay from "./components/SummaryDisplay";

function App() {
  // const [summary, setSummary] = useState("");

  return (
    <div className="App" style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>AI Powered Earnings Call Analyzer</h1>
      <FileUpload />
    </div>
  );
}

export default App;
