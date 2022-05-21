const toggleForm = () => {
    const container = document.querySelector(".container");  
  
    if (container.classList.contains("active")){
        container.classList.remove("active");
      // section.setAttribute("style", "background-color: #fee648")
      return;
    }
    container.classList.add("active");
    // section.setAttribute("style", "background-color: #e23139")
  }
  
  const toggleLinks = Array.from(document.querySelectorAll(".signup a"));
  
  toggleLinks.forEach(toggleLink => {
    toggleLink.addEventListener("click", toggleForm)
  })