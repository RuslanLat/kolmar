import json
from st_aggrid import AgGrid, JsCode, ColumnsAutoSizeMode, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder


with open("app/css/AG_GRID_LOCALE_RU.txt", "r") as f:
    AG_CRID_LOCALE_RU = json.load(f)


def plot_change_table(df, key):
    js = JsCode(
        """
            function(e) {
                let api = e.api;     
                let sel = api.getSelectedRows();
                api.applyTransaction({remove: sel});
            };
            """
    )

    gd = GridOptionsBuilder.from_dataframe(df, columns_auto_size_mode=0)
    gd.configure_pagination(
        enabled=True, paginationAutoPageSize=False, paginationPageSize=10
    )
    gd.configure_grid_options(stopEditingWhenCellsLoseFocus=True)  # , rowHeight=80
    gd.configure_grid_options(localeText=AG_CRID_LOCALE_RU)
    gd.configure_default_column(editable=True, groupable=True)
    gd.configure_selection(selection_mode="multiple", use_checkbox=True)
    gd.configure_grid_options(onRowSelected=js, pre_selected_rows=[])
    gridoptions = gd.build()
    grid_table = AgGrid(
        df,
        gridOptions=gridoptions,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        allow_unsafe_jscode=True,
        theme="alpine",
        key=key,
    )

    return grid_table