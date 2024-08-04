import { invoke } from "@tauri-apps/api/tauri";

export async function handleBinConv(input, outputType) {
  const num = parseInt(input);
  const binRegex = /^[01]+$/;

  if (isNaN(num) || !binRegex.test(input)) {
    return "IE";
  } else {
    try {
      switch (outputType) {
        case "OCT":
          return String(await invoke("b2o", { x: num }));
        case "DEC":
          return String(await invoke("b2d", { x: num }));
        case "HEX":
          return await invoke("b2h", { x: num });
      }
    } catch (error) {
      console.error("Error invoking Tauri command:", error);
      return "";
    }
  }
}

export async function handleOctConv(input, outputType) {
  const num = parseInt(input);
  const octRegex = /^[0-7]+$/;

  if (isNaN(num) || !octRegex.test(input)) {
    return "IE";
  } else {
    try {
      switch (outputType) {
        case "BIN":
          return String(await invoke("o2b", { x: num }));
        case "DEC":
          return String(await invoke("o2d", { x: num }));
        case "HEX":
          return await invoke("o2h", { x: num });
      }
    } catch (error) {
      console.error("Error invoking Tauri command:", error);
      return "";
    }
  }
}

export async function handleDecConv(input, outputType) {
  const num = parseInt(input);
  const decRegex = /^[0-9]+$/;

  if (isNaN(num) || !decRegex.test(input)) {
    return "IE";
  } else {
    try {
      switch (outputType) {
        case "BIN":
          return String(await invoke("d2b", { x: num }));
        case "OCT":
          return String(await invoke("d2o", { x: num }));
        case "HEX":
          return await invoke("d2h", { x: num });
      }
    } catch (error) {
      console.error("Error invoking Tauri command:", error);
      return "";
    }
  }
}

export async function handleHexConv(input, outputType) {
  const hexRegex = /^[0-9A-Fa-f]+$/;

  if (!hexRegex.test(input)) {
    return "IE";
  } else {
    try {
      switch (outputType) {
        case "BIN":
          return await invoke("h2b", { x: input });
        case "OCT":
          return await invoke("h2o", { x: input });
        case "DEC":
          return await invoke("h2d", { x: input });
      }
    } catch (error) {
      console.error("Error invoking Tauri command:", error);
      return "";
    }
  }
}
