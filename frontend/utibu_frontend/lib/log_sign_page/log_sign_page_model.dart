import '/flutter_flow/flutter_flow_util.dart';
import 'log_sign_page_widget.dart' show LogSignPageWidget;
import 'package:flutter/material.dart';

class LogSignPageModel extends FlutterFlowModel<LogSignPageWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
  }
}
