import streamlit as st
import pandas as pd
import pydeck as pdk
from pandas import DataFrame
from snowflake.snowpark.context import get_active_session
import settings

session = get_active_session()

@st.cache_data
def geo_data(_cs) -> DataFrame:
	sql = f"select lat, long from retail.public.store"
	data = _cs.sql(sql).collect()
	return pd.DataFrame(
		data,
		columns=['lat', 'long'])


chart_data = geo_data(session)
st.pydeck_chart(
	pdk.Deck(
		map_provider=None,
		map_style=None,
		initial_view_state=pdk.ViewState(
			latitude=40.94937,
			longitude=-73.82475,
			zoom=11,
			pitch=50,
		),
	layers=[
		pdk.Layer(
			'HexagonLayer',
			data=chart_data,
			get_position='[long, lat]',
			radius=200,
			elevation_scale=4,
			elevation_range=[0, 1000],
			pickable=True,
			extruded=True,
		),
		pdk.Layer(
			'ScatterplotLayer',
			data=chart_data,
			get_position='[long, lat]',
			get_color='[200, 30, 0, 160]',
			get_radius=200,
			),
		],
	)
)


#@st.cache_data
#def store_data(_cs):
#	sql = f"select * from retail.public.store limit 10"
#	data = _cs.sql(sql).collect()
#	return pd.DataFrame(
#		data
#	)
#df = store_data(session)
#for column in df.columns:
#	st.text(f"{column}: {df.at[0, column]}")



#sql = (
#	"WITH input AS ( SELECT { 'county': retail.public.store.county, 'city': retail.public.store.city} AS categorical_dimensions, {'bear_year_data': retail.public.store.beer_year_data} AS continuous_dimensions, retail.public.store.store_year_data, False as label) SELECT res.* FROM input, TABLE(SNOWFLAKE.ML.TOP_INSIGHTS( input.categorical_dimensions, input.continuous_dimensions, CAST(input.metric AS FLOAT), input.label ) OVER (PARTITION BY 0) ) res ORDER BY res.surprise DESC;"
#)
#st_df = session.sql(sql).collect()
#final_df = pd.DataFrame(
#		st_df,
#		columns=['CONTRIBUTOR', 'METRIC_CONTROL', 'METRIC_TEST', 'SURPRISE', 'RELATIVE_CHANGE', 'GROWTH_RATE', 'EXPECTED_METRIC_TEST', 'OVERALL_METRIC_CONTROL', 'OVERALL_METRIC_TEST', 'OVERALL_GROWTH_RATE', 'NEW_IN_TEST', 'MISSING_IN_TEST'])
#
#st.text(final_df.to_string())
