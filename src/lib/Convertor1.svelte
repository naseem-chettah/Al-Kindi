<script>
  import { invoke } from "@tauri-apps/api/tauri";

  let userInputType = "dec";
  let outputType = "bin";
  let outputTypes = ["bin", "oct", "hex"];
  let outputValue;
  $: text = userInputType === "hex";

  function handleChangeType() {
    switch (userInputType) {
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
    outputType = outputTypes[0];
    const input = document.getElementById("input");
    input.value = "";
    outputValue = "";
  }

  function handleInputChange(e) {
    switch (userInputType) {
      /* case "bin":
        handleBinConv(e.target.value);
        break;
      case "oct":
        handleOctConv(e.target.value);
        break; */
      case "dec":
        handleDecConv(e.target.value);
        break;
      /* case "hex":
        handleHexConv(e.target.value);
        break; */
    }
  }

  async function handleDecConv(userInput) {
    const num = parseInt(userInput, 10);
    if (isNaN(num)) {
      const input = document.getElementById("input");
      input.value = "";
      outputValue = "";
      return;
    }

    switch (outputType) {
      case "bin":
        outputValue = String(await invoke("d2b", { x: num }));
        break;
      case "oct":
        outputValue = String(await invoke("d2o", { x: num }));
        break;
      case "hex":
        outputValue = await invoke("d2h", { x: num });
        break;
    }
  }
</script>

<main class="flex justify-center">
  <div class="grid grid-cols-4 min-w-[50%] m-5">
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
      bind:value={userInputType}
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
</main>
