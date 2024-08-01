from homeassistant.helpers import config_entry_flow

DOMAIN = "hisense_climate"

async def async_setup(hass, config):
    return True

async def async_setup_entry(hass, entry):
    hass.data[DOMAIN] = entry.data
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "climate"))
    return True

async def async_unload_entry(hass, entry):
    await hass.config_entries.async_forward_entry_unload(entry, "climate")
    hass.data.pop(DOMAIN)
    return True