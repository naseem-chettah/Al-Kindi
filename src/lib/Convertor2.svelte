<script>
  import {
    handleBinConv,
    handleOctConv,
    handleDecConv,
    handleHexConv,
  } from "$lib/utils/ConvertValues.js";

  let inputType;
  let outputs = ["", "", ""];

  let outputTypes = ["###", "###", "###"];

  $: {
    switch (inputType) {
      case "BIN":
        clearInputs();
        outputTypes = ["OCT", "DEC", "HEX"];
        break;
      case "OCT":
        clearInputs();
        outputTypes = ["BIN", "DEC", "HEX"];
        break;
      case "DEC":
        clearInputs();
        outputTypes = ["BIN", "OCT", "HEX"];
        break;
      case "HEX":
        clearInputs();
        outputTypes = ["BIN", "OCT", "DEC"];
        break;
    }
  }

  function clearInputs() {
    const inputElement = document.getElementById("input");
    inputElement.value = "";
    outputs = ["", "", ""];
  }

  async function handleInputChange(e) {
    const input = e.target.value.toUpperCase();

    switch (inputType) {
      case "BIN":
        outputs[0] = await handleBinConv(input, outputTypes[0]);
        outputs[1] = await handleBinConv(input, outputTypes[1]);
        outputs[2] = await handleBinConv(input, outputTypes[2]);
        break;
      case "OCT":
        outputs[0] = await handleOctConv(input, outputTypes[0]);
        outputs[1] = await handleOctConv(input, outputTypes[1]);
        outputs[2] = await handleOctConv(input, outputTypes[2]);
        break;
      case "DEC":
        outputs[0] = await handleDecConv(input, outputTypes[0]);
        outputs[1] = await handleDecConv(input, outputTypes[1]);
        outputs[2] = await handleDecConv(input, outputTypes[2]);
        break;
      case "HEX":
        outputs[0] = await handleHexConv(input, outputTypes[0]);
        outputs[1] = await handleHexConv(input, outputTypes[1]);
        outputs[2] = await handleHexConv(input, outputTypes[2]);
        break;
    }
    if (outputs[0] == "IE") {
      clearInputs();
    }
  }
</script>

<div class="input-type flex justify-center">
  <label class="m-2" for="options">Numeric Base: </label>
  <div class="options m-2" name="options">
    <input type="radio" name="option" value="BIN" bind:group={inputType} /> BIN
    <input type="radio" name="option" value="OCT" bind:group={inputType} /> OCT
    <input type="radio" name="option" value="DEC" bind:group={inputType} /> DEC
    <input type="radio" name="option" value="HEX" bind:group={inputType} /> HEX
  </div>
</div>

<div class="input flex justify-center align-middle">
  <label class="p-2 mx-2" for="input">Input:</label>
  <input
    class="p-2 mx-2 border-b border-b-gruv-black-l outline-none"
    type="text"
    name="input"
    id="input"
    on:input={handleInputChange}
  />
</div>
<div class="output">
  <div class="p-2 mx-2 flex justify-center">
    <label for="output1">{outputTypes[0]}: </label>
    <input
      class="p-2 mx-2 border-b border-b-gruv-black-l outline-none"
      type="text"
      name="output1"
      bind:value={outputs[0]}
      readonly
    />
  </div>
  <div class="p-2 mx-2 flex justify-center">
    <label for="output2">{outputTypes[1]}: </label>
    <input
      class="p-2 mx-2 border-b border-b-gruv-black-l outline-none"
      type="text"
      name="output2"
      bind:value={outputs[1]}
      readonly
    />
  </div>
  <div class="p-2 mx-2 flex justify-center">
    <label for="output3">{outputTypes[2]}: </label>
    <input
      class="p-2 mx-2 border-b border-b-gruv-black-l outline-none"
      type="text"
      name="output3"
      bind:value={outputs[2]}
      readonly
    />
  </div>
</div>
