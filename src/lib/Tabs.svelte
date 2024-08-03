<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  export let tabs;
  export let activeTab;
</script>

<ul class="tabs flex justify-evenly">
  {#each tabs as tab}
    <li>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div
        on:click={() => dispatch("tabChange", tab)}
        class:active={tab === activeTab}
      >
        {tab}
      </div>
    </li>
  {/each}
</ul>
