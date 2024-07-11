<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  export let tabs;
  export let activeTab;
</script>

<div class="tabs min-w-[50%]">
  <ul class="flex justify-evenly px-32">
    {#each tabs as tab}
      <li on:click={() => dispatch('tabChange', tab)}>
        <div class:active={tab === activeTab}>{tab}</div>
      </li>
    {/each}
  </ul>
</div>
