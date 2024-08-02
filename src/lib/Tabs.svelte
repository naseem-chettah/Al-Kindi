<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  export let tabs;
  export let activeTab;
</script>

<div class="tabs min-w-[50%]">
  <ul class="flex justify-evenly px-32">
    {#each tabs as tab}
      <li>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <div on:click={() => dispatch('tabChange', tab)} class:active={tab === activeTab}>{tab}</div>
      </li>
    {/each}
  </ul>
</div>
