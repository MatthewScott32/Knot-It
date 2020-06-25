document.querySelector("#knot").addEventListener("change", evt => {
    let knotId = evt.target.value
    window.location.href = `?knot=${knotId}`
})