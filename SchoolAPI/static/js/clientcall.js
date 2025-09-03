$(document).ready(function(){
    $.ajax({
        url: "https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/Schools/FeatureServer/0/query?where=1%3D1&objectIds=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=*&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&collation=&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnTrueCurves=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token=",
        type: "GET",
        datatype: "json",
        success: function(response){
            console.log(response)
            var rows = ""

            $.each(response.features, function(index, school) {
                rows += "<tr><td>" + 
                    school.attributes.school_name + "</td>" +
                    "<td>" + school.attributes.grade_level + "</td>"  +
                    "<td>" + school.attributes.type_specific + "</td></tr>"
            })

            $("#tbSchool tbody").html(rows)
        },
        error: function(error) {
            console.log(error)
        }
    })

});