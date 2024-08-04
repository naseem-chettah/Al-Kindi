<script>
  import { handleBinConv, handleOctConv, handleDecConv, handleHexConv } from "$lib/utils/ConvertValues";

  let inputType = "dec";
  let outputTypes = ["bin", "oct", "hex"];
  let outputType = outputTypes[0];
  let outputValue;
  $: text = inputType === "hex";

  function handleChangeType() {
    switch (inputType) {
      case "bin":
        outputTypes = ["oct", "dec", "hex"];
        break;
      case "oct":
        outputTypes = ["bin", "dec", "hex"];
        break;
      case "dec":
        outputTypes = ["bin", "oct", "hex"];
        break;
      case "hex":
        outputTypes = ["bin", "oct", "dec"];
        break;
    }

    if (outputType === inputType) {
      outputType = outputTypes[0];
    }

    const input = document.getElementById("input");
    input.value = "";
    outputValue = "";
  }

  async function handleInputChange(e) {
    switch (inputType) {
      case "bin":
        outputValue = await handleBinConv(
          e.target.value,
          outputType.toUpperCase(),
        );
        break;
      case "oct":
        outputValue = await handleOctConv(
          e.target.value,
          outputType.toUpperCase(),
        );
        break;
      case "dec":
        outputValue = await handleDecConv(
          e.target.value,
          outputType.toUpperCase(),
        );
        break;
      case "hex":
        e.target.value = e.target.value.toUpperCase();
        outputValue = await handleHexConv(
          e.target.value,
          outputType.toUpperCase(),
        );
        break;
    }
  }
</script>

<div class="grid grid-cols-4 m-2">
  <input
    class="p-2 m-2 border-b border-b-gruv-black-l outline-none col-span-3"
    type={text ? "text" : "number"}
    id="input"
    on:input={handleInputChange}
  />
  <select
    class="p-2 m-2 border border-gruv-black-l bg-white rounded outline-none"
    name="input-type"
    id="input-type"
    bind:value={inputType}
    on:change={handleChangeType}
  >
    <option value="bin">BIN</option>
    <option value="oct">OCT</option>
    <option value="dec" selected>DEC</option>
    <option value="hex">HEX</option>
  </select>
  <select
    class="p-2 m-2 border border-gruv-black-l bg-white rounded outline-none"
    name="output-type"
    id="output-type"
    bind:value={outputType}
    on:change={handleChangeType}
  >
    {#each outputTypes as type}
      <option value={type}>{type.toUpperCase()}</option>
    {/each}
  </select>
  <input
    class="p-2 m-2 border-b border-b-gruv-black-l outline-none col-span-3"
    readonly
    id="output"
    type="text"
    bind:value={outputValue}
  />
</div>
