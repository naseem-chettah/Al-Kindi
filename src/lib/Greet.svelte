<script>
  import { invoke } from "@tauri-apps/api/tauri";

  let x;
  let result;

  async function d2b() {
    result = await invoke("d2b", { x });
  }
</script>

<div>
  <input type="number" id="greet-input" placeholder="Enter a name..." bind:value={x} />
  <button on:click={d2b}>To BIN</button>
  <p>{result}</p>
</div>
