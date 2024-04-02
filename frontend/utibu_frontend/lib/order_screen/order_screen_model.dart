import '/flutter_flow/flutter_flow_util.dart';
import 'order_screen_widget.dart' show OrderScreenWidget;
import 'package:flutter/material.dart';

class OrderScreenModel extends FlutterFlowModel<OrderScreenWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // State field(s) for search widget.
  FocusNode? searchFocusNode;
  TextEditingController? searchController;
  String? Function(BuildContext, String?)? searchControllerValidator;
  // State field(s) for CountController widget.
  int? countControllerValue1;
  // State field(s) for Checkbox widget.
  bool? checkboxValue1;
  // State field(s) for CountController widget.
  int? countControllerValue2;
  // State field(s) for Checkbox widget.
  bool? checkboxValue2;
  // State field(s) for CountController widget.
  int? countControllerValue3;
  // State field(s) for Checkbox widget.
  bool? checkboxValue3;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
    searchFocusNode?.dispose();
    searchController?.dispose();
  }
}
