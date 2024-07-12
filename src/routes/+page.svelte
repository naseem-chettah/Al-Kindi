<script>
  import Tabs from "../lib/Tabs.svelte";
  import Convertor1 from "../lib/Convertor1.svelte";
  import Convertor2 from "../lib/Convertor2.svelte";

  let tabs = ["Convertor 1", "Convertor 2", "Ciphering"];
  let activeTab = "Convertor 1";

  const tabChange = (e) => {
    activeTab = e.detail;
  };
</script>

<main>
  <div class="flex justify-center">
    <div class="min-w-[50%] m-5">
      <img
        class="max-h-56 w-full object-cover"
        src="src/static/img/banner.jpg"
        alt="banner"
      />
    </div>
  </div>
  <Tabs {tabs} {activeTab} on:tabChange={tabChange} />
  {#if activeTab === "Convertor 1"}
    <Convertor1 />
  {:else if activeTab === "Convertor 2"}
    <Convertor2 />
  {:else if activeTab === "Ciphering"}
    <p>Ciphering</p>
  {:else}
    error
  {/if}
</main>
